from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def search():
    # 解析请求中的关键词
    keywords = request.json.get('keywords', '')
    
    # 配置Selenium使用Chrome的无头模式
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    
    # 初始化WebDriver
    driver = webdriver.Chrome(chrome_options=chrome_options)
    
    # 打开URL
    driver.get("http://example.com") # 替换为您的目标URL
    
    try:
        # 在输入框中输入关键词并按回车
        input_element = driver.find_element_by_name("q") # 替换为实际的输入框元素名称或ID
        input_element.send_keys(keywords + Keys.RETURN)
        
        time.sleep(2) # 等待页面加载
        
        # 抓取列表元素的文本
        texts = [element.text for element in driver.find_elements_by_xpath("//li")] # 替换为实际的列表元素XPath
        
        return jsonify({"texts": texts})
    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
