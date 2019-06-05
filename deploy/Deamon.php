<?php

/****
 * @author handongjie
 * @datetime 2019年2月14日 下午3:42:29
 * @comment( comment='php cli守护进程' )
 */

class Deamon
{
    private $_pidFile;
    private $_jobs = [];
    private $_infoDir;
    
    const TASK_CLASS_NAME = 'Task';
    const TASK_ENTRANCR_METHOD = 'entrance';
    const TASK_JOB_NAME = 'task_job_queue';
    
    public function __construct( $dir = '/tmp' )
    {
        $this->_setInfoDir( $dir );
        $this->_pidFile = rtrim( $this->_infoDir, '/' ) . '/' . self::TASK_JOB_NAME . '_pid.log';
        $this->_checkPcntl();
    }
    
    /****
     * @author( author='islandman' )
     * @date( date = '2019年2月14日' )
     * @comment( comment = '后台运行' )
     * @method( method = '' )
     * @op( op = '' )
     */
    private function _demonize()
    {
        if ( php_sapi_name() != 'cli' )
        {
            exit('Should run in CLI');
        }
        
        $pid = pcntl_fork();
        
        if ( $pid < 0 )
        {
            exit( "Can't Fork!" );
        }
        elseif( $pid > 0 )
        {
            exit();
        }
        
        if ( posix_setsid() === -1 )
        {
            exit( 'Could not detach' );
        }
        
        chdir( '/' );
        umask( 0 );
        
        $fp = fopen( $this->_pidFile, 'w' ) or exit( "Can't create pid file" );
        
        fwrite( $fp, posix_getpid() );
        fclose( $fp );
        
        //由于守护进程用不到标准输入输出，关闭标准输入，输出，错误输出描述符
        fclose( STDIN );
        fclose( STDOUT );
        fclose( STDERR );
        
        call_user_func( [ self::TASK_CLASS_NAME, self::TASK_ENTRANCR_METHOD ] );
        
        return;
    }
    
    /****
     * @author( author='islandman' )
     * @date( date = '2019年2月14日' )
     * @comment( comment = '' )
     * @method( method = '' )
     * @op( op = '' )
     * @param string $dir
     */
    private function _setInfoDir( $dir = null )
    {
        if ( is_dir( $dir ) )
        {
            $this->_infoDir = $dir;
        }
        else
        {
            $this->_infoDir = __DIR__;
        }
    }
    
    /****
     * @author( author='islandman' )
     * @date( date = '2019年2月14日' )
     * @comment( comment = '' )
     * @method( method = '' )
     * @op( op = '' )
     */
    private function _checkPcntl()
    {
        !function_exists( 'pcntl_signal' ) && exit( 'Error:Need PHP Pcntl extension!' );
    }
    
    /****
     * @author( author='islandman' )
     * @date( date = '2019年2月14日' )
     * @comment( comment = '' )
     * @method( method = '' )
     * @op( op = '' )
     * @return number
     */
    private function _getPid()
    {
        if ( !file_exists( $this->_pidFile ) )
        {
            return 0;
        }
        
        $pid = intval( file_get_contents( $this->_pidFile ) );
        
        if ( posix_kill( $pid, SIG_DFL ) )
        {
            return $pid;
        }
        else
        {
            unlink( $this->_pidFile );
            
            return 0;
        }
    }
    
    /****
     * @author( author='islandman' )
     * @date( date = '2019年2月14日' )
     * @comment( comment = '' )
     * @method( method = '' )
     * @op( op = '' )
     * @param string $message
     */
    private function _message( $message )
    {
        printf( "%s  %d %d  %s" . PHP_EOL, date( "Y-m-d H:i:s" ), posix_getpid(), posix_getppid(), $message );
    }
    
    /****
     * @author( author='islandman' )
     * @date( date = '2019年2月14日' )
     * @comment( comment = '' )
     * @method( method = '' )
     * @op( op = '' )
     */
    public function start()
    {
        if ( $this->_getPid() > 0 )
        {
            $this->_message( 'Running' );
        }
        else
        {
            $this->_demonize();
            $this->_message( 'Start' );
        }
    }
    
    /****
     * @author( author='islandman' )
     * @date( date = '2019年2月14日' )
     * @comment( comment = '' )
     * @method( method = '' )
     * @op( op = '' )
     */
    public function stop()
    {
        $pid = $this->_getPid();
        
        if ( $pid > 0 )
        {
            posix_kill( $pid, SIGTERM );
            unlink( $this->_pidFile );
            
            echo 'Stoped' . PHP_EOL;
        }
        else
        {
            echo "Not Running" . PHP_EOL;
        }
    }
    
    /****
     * @author( author='islandman' )
     * @date( date = '2019年2月14日' )
     * @comment( comment = '' )
     * @method( method = '' )
     * @op( op = '' )
     */
    public function status()
    {
        if ( $this->_getPid() > 0 )
        {
            $this->_message( 'Is Running' );
        }
        else
        {
            echo 'Not Running' . PHP_EOL;
        }
    }
    
    /***
     * @author( author='islandman' )
     * @date( date = '2019年2月14日' )
     * @comment( comment = '' )
     * @method( method = '' )
     * @op( op = '' )
     * @param array $jobs
     */
    public function addJobs( $jobs = [] )
    {
        if ( !isset( $jobs[ 'function' ] ) || 
            empty( $jobs[ 'function' ] ) ) 
        {
            $this->_message( 'Need function param' );
        }
        
        if ( !isset( $jobs[ 'argv' ] ) || 
            empty( $jobs[ 'argv' ] ) )
        {
            $jobs[ 'argv' ] = "";
        }
        
        $this->_jobs[] = $jobs;
    }
    
    /****
     * @author( author='islandman' )
     * @date( date = '2019年2月14日' )
     * @comment( comment = '' )
     * @method( method = '' )
     * @op( op = '' )
     * @param array $argv
     */
    public function run( array $argv )
    {
        $param = is_array( $argv ) ? $argv[ 1 ] : null;
        
        switch ( $param )
        {
            case 'start':
                $this->start();
                break;
            case 'stop':
                $this->stop();
                break;
            case 'status':
                $this->status();
                break;
            default:
                echo "Argv start|stop|status " . PHP_EOL;
                break;
        }
    }
}

/****
 * @author islandman
 * @datetime 2019年2月14日 下午4:23:44
 * @comment( comment='' )
 */
class Rdb
{
    private $_arrRedisCfg = [
        'local' => [
            'host' => '82e36baa51ae',
            'port' => 6379,
            'password' => null,
            'index' => 1,
        ],
        
        'production' => [
            'host' => 'r-rj920afd62762f74.redis.rds.aliyuncs.com',
            'port' => 'Kfwx5uGVkv',
            'password' => 6379,
            'index' => 1,
        ],
    ];
    
    const APP_ENV = 'APP_ENV';
    
    const PROD_MODE = 'production';
    
    public static $ins = null;
    
    public static $redisConn = null;
    
    /****
     * @author( author='islandman' )
     * @date( date = '2019年2月14日' )
     * @comment( comment = '实例化redis' )
     * @method( method = '' )
     * @op( op = '' )
     */
    private function __construct()
    {
        if( null == self::$redisConn )
        {
            $strEnv = getenv( self::APP_ENV );
            
            $objRedis = new \Redis();
            $objRedis->connect( $this->_arrRedisCfg[ $strEnv ][ 'host' ],
                $this->_arrRedisCfg[ $strEnv ][ 'port' ] );
            
            if( self::PROD_MODE == $strEnv )
            {
                $objRedis->auth( $this->_arrRedisCfg[ $strEnv ][ 'password' ] );
            }
            
            $objRedis->select( $this->_arrRedisCfg[ $strEnv ][ 'index' ] );
            
            self::$redisConn = $objRedis;
        }
    }
    
    /****
     * @author( author='islandman' )
     * @date( date = '2019年2月14日' )
     * @comment( comment = '实例化对象并生成redis' )
     * @method( method = '' )
     * @op( op = '' )
     * @return \Redis
     */
    public static function getIns()
    {
        if( null == self::$ins )
        {
            self::$ins = new Rdb();
        }
        
        return self::$redisConn;
    }
}

/****
 * @author islandman
 * @datetime 2019年2月14日 下午4:43:10
 * @comment( comment='' )
 */
class Task
{
    const UPDATE_SITE_CASE = 'update_site_case';
    
    const SITE_UPDATE_CASE_QUEUE = 's_site_update_queue';
    
    const THREAD_NUMS = 20;
    
    const SLEEP_TIME = 1;
    
    const APP_ENV = 'APP_ENV';
    
    const UPDATE_SITE_CASE_QUEUE = 'l_update_site_queue';
    
    const ERR_MSG = 'The required param is empty!!!';
    
    public static $ins = null;
    
    private static $_arrWorkDir = [
        /*pro mode*/
        'local' => '/data/www/cs_out_site/deploy',
        
        /*dev mode*/
        'production' => '/export/data/tomcatRoot/customer.orderplus.com/deploy',
    ];
    
    private static $_env = null;
    
    private function __construct()
    {
        if( null == self::$_env )
        {
            self::$_env = getenv( self::APP_ENV );
        }
    }
    
    /****
     * @author( author='islandman' )
     * @date( date = '2019年2月14日' )
     * @comment( comment = '入口' )
     * @method( method = '' )
     * @op( op = '' )
     */
    public static function entrance()
    {
        if( null == self::$ins )
        {
            self::$ins = new Task();
        }
        
        $objRedis = Rdb::getIns();
        
        /****
        switch( $strAction )
        {
            case self::UPDATE_SITE_CASE:
                while ( TRUE )
                {
                    if( $objRedis->lSize( self::UPDATE_SITE_CASE_QUEUE ) > 0 )
                    {
                        $iSiteId = $objRedis->rPop( self::UPDATE_SITE_CASE_QUEUE );
                        $this->_updateSiteCase( $iSiteId );
                    }
                    
                    //sleep( self::SLEEP_TIME );
                }
                break;
                
            default:
                exit( self::ERR_MSG );
                break;
        }
        ****/
        
        while ( TRUE )
        {
            if( $objRedis->lSize( self::UPDATE_SITE_CASE_QUEUE ) > 0 )
            {
                $iSiteId = $objRedis->rPop( self::UPDATE_SITE_CASE_QUEUE );
                self::_updateSiteCase( $objRedis, $iSiteId );
            }
            
            sleep( self::SLEEP_TIME );
        }
    }
    
    /***
     * @author( author='islandman' )
     * @date( date = '2019年2月14日' )
     * @param object $objRedis
     * @param integer $iSiteId
     * @comment( comment = '批量更新站点的case' )
     * @method( method = '' )
     * @op( op = '' )
     */
    private static function _updateSiteCase( \Redis $objRedis, $iSiteId )
    {
        try {
            $strKey = self::SITE_UPDATE_CASE_QUEUE;
            $objRedis->sAdd( $strKey, $iSiteId );
            
            $iThreadNums = self::THREAD_NUMS;
            $strLogFile = '/tmp/pull_dispute.' . date( 'Ymd', time() ) . '.log';
            
            if( !file_exists( $strLogFile ) )
            {
                //fopen( $strLogFile, 'r+' );
                file_put_contents( $strLogFile, '----start log-----' . PHP_EOL . FILE_APPEND );
                //touch( $strLogFile );
                chmod( $strLogFile, 0777 );
            }
            
            chdir( self::$_arrWorkDir[ self::$_env ] );
            $strExecFileName = './PullDispute.py';
            
            if( !is_executable( $strExecFileName ) )
            {
                chmod( $strExecFileName, 0777 );
            }
            
            $strCmd = 'python3 ' . $strExecFileName . ' ' . $iSiteId;
            $strCmd .= " {$iThreadNums} " . '>> ' . $strLogFile . ' & ';
            
            file_put_contents( '/tmp/str_cmd.log', var_export( $strCmd, true ) . PHP_EOL, FILE_APPEND );
            
            shell_exec( $strCmd );
        }
        catch( \Exception $e )
        {
            file_put_contents( "/tmp/case.log",
                var_export( __FILE__ . __NAMESPACE__ .
                    __CLASS__ . __METHOD__ . __LINE__ . $e->getTrace() .
                    $e->getMessage() . $e->getTraceAsString(), true ) . PHP_EOL,
                FILE_APPEND );
            
            throw new \Exception( __FILE__ . __NAMESPACE__ .
                __CLASS__ . __METHOD__ . __LINE__ . $e->getTrace() .
                $e->getMessage() . $e->getTraceAsString() );
        }
    }
}

$deamon = new Deamon();
$deamon->run( $argv );