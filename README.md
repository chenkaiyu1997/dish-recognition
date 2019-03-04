## Dish Recognition Project


### 架构说明

<img src="https://github.com/chenkaiyu1997/dish-recognition/blob/master/structure.png" width="500"/>

* 前端基于Wepy的微信小程序开发，并使用了Vant-weapp的组件
* ObjectDetection模型基于yolo-keras库开发
* 后端推荐使用Python-Flask，接收请求后先调用Detection框架，再调用LeonardoAPI，再通过sqlalchemy访问数据库



### Code Structure

* getfeature
  * 文件夹包含一个Python脚本，将目标文件夹的图片上传到LeonardoAPI并得到feature vector并保存
* frontend 
  * 文件夹包含前端代码，请先运行 npm install，然后再参照微信小程序开发指南，运行微信开发者工具
* detection 
  * 文件夹包含Yolo模型的操作代码，能将一张图片中的碗识别出来，并切分成不同的图片。请先参照README下载模型后再参照示例代码运行


### Tasks

* Segmentation

  - [x] 分析DarkNet，写服务器代码自动调用
  - [x] 得到DarkNet的结果并进行图片裁剪
  - [x] 将得到的图片调用Leonardo云端API返回
  - [x] 将得到的返回值FeatureVector给下一步处理

* Feature Processing

  - [ ] 将得到的Feature Vector与数据库中的数据进行相似度比较
  - [ ] 返回对应的菜品信息
  - [ ] 顺带写一个简单的数据库管理脚本/界面

* 前端界面，后端Server的交互

  - [x] 拍照+上传图片
  - [x] 接收后端数据，展示后端返回的信息页面
  - [ ] 前后端数据连通
  
