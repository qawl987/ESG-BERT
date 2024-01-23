# ESG-BERT-analyzing-Reports

## 目標
在專案中我們應用ESG-BERT分析美國及台灣各25家頂尖公司在各自的年度ESG report 中關於Sustainable Investing中26個領域的貢獻。
透過NLP技術以及PDF汲取資訊，分析出不同公司側重的領域，以及台美差異。

## 結果
透過ESG-BERT輸出的label製成雷達圖比較，可看出與其他公司平均的差異，可能是該公司需要補強的部分
![full 25 company compare](https://user-images.githubusercontent.com/62208230/228335894-946aa47e-2405-4877-accc-364348c106e4.png)
![21_microsoft_1_89_company vs  average](https://user-images.githubusercontent.com/62208230/228335629-ddd76593-c13b-474b-9e54-d92b77583e86.png)
![04_apple_1_72_company vs  average](https://user-images.githubusercontent.com/62208230/228335664-e6f395ad-b137-46b9-9b2e-6fc21c3ec9e1.png)

## 資料預處理
先將PDF利用Foxit editor轉成XML格式，如此一個段落就可以用一個tag如<p>提取
![image](https://user-images.githubusercontent.com/62208230/228408894-a65426d7-06b0-489a-ace3-206404dc598f.png)
最後選擇只保留<p>，因為其他tag大多太短或資訊不完整，會影響判斷
接著把一段段<p>，移除ASCII以外的符號

## 模型應用
將預處理後的多段文字送進esg-bert，得到多個label後存成csv檔

## 詞頻比較
由於esg-bert的作者在他的文章中提到，esg-bert也算是找關鍵字的模型，因此我們選擇用經典詞頻統計的方式作為比較方法。先透過chat-gpt在26個領域生成25個one-word的關鍵字，比較哪個label在一段文字中有最多的關鍵字出現，就將該段文字定為該label;而若一個關鍵字都沒出現則為None

## 分析
蒐集完模型與詞頻的數據後發現在詞頻輸出為None且文字字數少於十個時，esg-bert容易輸出無意義label，因此可以將該句移除csv中，即使用詞頻幫助我們進一步優化esg-bert的結果
![image](https://user-images.githubusercontent.com/62208230/228411149-8c63645f-e109-4175-b59f-2b7e87eb34a9.png)

## 運行
main.ipynb >> pdf >> text >> paragraph.txt >> ESGBERT >> output.txt >> csv
1. 先透過pdfminer將pdf轉成文字
2. 經過https://github.com/mukut03/ESG-BERT 模型產生預測的esg label
3. 最後一個cell將產生的output.txt與轉換出的paragraph一起產生帶有label標籤的csv
