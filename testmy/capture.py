from selenium import webdriver
import time


def capture(url, filename="capture.png"):
    browser = webdriver.Chrome(r"D:\chromedriver\chromedriver.exe")
    browser.set_window_size(1400, 900)
    browser.get(url)  # Load page
    browser.execute_script("""
    (function () {
      var y = 0;
      var step = 100;
      window.scroll(0, 0);

      function f() {
        if (y < document.body.scrollHeight) {
          y += step;
          window.scroll(0, y);
          setTimeout(f, 50);
        } else {
          window.scroll(0, 0);
          document.title += "scroll-done";
        }
      }

      setTimeout(f, 1000);
    })();
  """)

    for i in range(30):
        if "scroll-done" in browser.title:
            break
        time.sleep(2)
    beg = time.time()
    for i in range(10):
        browser.save_screenshot(filename)
    end = time.time()
    print(end - beg)
    browser.close()


capture("https://t.17track.net/zh-cn#nums=788256331036")