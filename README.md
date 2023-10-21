## Django架構
MTV (Model-Template-View) in Django:
- Model: 同MVC中的Model，負責數據和業務邏輯。它與數據庫直接交互。
- Template: 對應於 MVC 中的 View，負責呈現數據給用戶。在 Django 中，這通常是一個HTML模板，用於定義如何顯示數據。
- View: 對應於 MVC 中的 Controller，負責處理用戶的請求，與 Model 交互，並選擇一個 Template 來呈現數據。在 Django 中，View 更多地描述了“哪些數據”要被呈現，而不是“如何”呈現這些數據。

## 使用方式指令
## step1 build project
```sh
django-admin startproject myproject
```

## step2 build django organiztion
```sh
python manage.py startapp myapp
```

## start project
```sh
python manage.py runserver 
```

## wsgi start project
```sh
gunicorn myproject.wsgi:application
```

## wsgi setting start project
```sh
gunicorn myproject.wsgi:application -c gunicorn.conf.py
```

## 建置db
> 根據model.py內容,紀錄CRUD的動作生成,這時還尚未建置table
```sh
python manage.py makemigrations myapp
```

> 檢查生成的CRUD的文件紀錄,確認無誤後根據文件紀錄的規格生成table
```sh
python manage.py migrate
```
這個命令將所有待執行的遷移應用到數據庫。這意味著它會修改數據庫結構，以使其與最新的模型結構保持一致。
結果: 數據庫結構會更新。例如，新的表可能會被創建，或者現有的表可能會被修改或刪除。



## 功能新增
- 新增Signals(@receiver)
    > 用途:CRUD操作成功與失敗都會有一個通知訊息
- 新增unit test
- 新增django表單
    > 網址: http://127.0.0.1:8000/profiles/create/
    > 用途1: 可以檢查前端表單的格式是否正確
    > 用途2: 替表單增加了CSRF的保護,以求安全性
    > 用途3: 簡化程式碼,且form.save可自動存取數據
- 新增generic view
    > 網址: http://127.0.0.1:8000/generic/
    > 用途:簡化重複繁瑣的程式碼，django針對於場景給出一個模板,即可省略該場景自己撰寫的程式
- 新增pagination
    > 網址: http://127.0.0.1:8000/pagination/items/
    > 用途: 得出來的List有分頁功能
- 新增多語系
    > 網址: http://localhost:8000/multilingual/
    > 用途: 支援多國語言
    > 
    ```sh

    $ apt-get install gettext
    $ python manage.py makemessages -l zh_Hant
    $ vim locale/zh_Hant/LC_MESSAGES/django.po
    >> msgid "Welcome to our website!"
    >> msgstr "歡迎來到我們的網站！"
    >> msgid "Home Page"
    >> msgstr "首頁"
    >> msgid "Change language"
    >> msgstr "更改語言"

    $ python manage.py compilemessages
    ```
- 新增ContentType
    > 網址: http://127.0.0.1:8000/contecttype/book/1/
    > 用途: 可以指定關聯哪一個表單
- 新增admin
    > 網址: http://localhost:8000/admin
    > 用途: 顯示所有已註冊的模型
    > 建立超級用戶權限
    ```sh
    python manage.py createsuperuser
    ```

- 新增多重資料庫
    > 用途: 指定資料放置的位置
    > 方式:
    >> 需在setting DATABASES設定db位置,需透過指定的方式過濾目標db需要建立的table，最後將設定的路定填寫至需在setting中的DATABASE_ROUTERS
    ```sh
    python manage.py makemigrations myapp
    python manage.py migrate myapp --database=other_database
    ```


## 語法紀錄
<details>
<summary>QuerySet</summary>

```py
# 取得所有記錄
all_people = Person.objects.all()

#根據條件篩選記錄
johns = Person.objects.filter(name='John')

# 排除符合條件的記錄
not_johns = Person.objects.exclude(name='John')

# 取得單一記錄
person = Person.objects.get(name='John')

# 排序記錄
people_sorted = Person.objects.order_by('-age')

#傳回指定欄位的值列表
Person.objects.values_list('name', flat=True)

# 計算記錄數量
Person.objects.count()

#檢查是否有符合條件的記錄
Person.objects.filter(name='John').exists()
```

</details>


<details>
<summary>進行模型驗證 clean</summary>

```py
from django.db import models
from django.core.exceptions import ValidationError

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def clean(self):
        if not self.title:
            raise ValidationError("文章標題不能為空")
        if not self.content:
            raise ValidationError("文章內容不能為空")
```

</details>


<details>
<summary>進行模型驗證 validators</summary>

```py
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_slug

def validate_no_sensitive_words(value):
    sensitive_words = ["badword1", "badword2", "badword3"]
    for word in sensitive_words:
        if word in value.lower():
            raise ValidationError(f"標題中包含敏感詞: {word}")

class Article(models.Model):
    title = models.CharField(max_length=200, validators=[validate_slug, validate_no_sensitive_words])
    content = models.TextField()

```

</details>

## 檔案介紹
manage.py:

位置: 專案的根目錄
用途: 是命令行的工具，用於執行與Django專案相關的多種任務，例如啟動開發伺服器、建立新的apps或執行資料庫遷移。
settings.py:

位置: 專案資料夾內 (如 myproject/myproject/settings.py)
用途: 包含專案的設定和配置，例如資料庫設定、靜態文件路徑、中間件列表等。
urls.py:

位置: 專案資料夾或app資料夾內
用途: 定義URL模式和路由，將特定的URL路徑映射到相對應的視圖函數或類。
views.py:

位置: app資料夾內
用途: 包含視圖函數或類，這些視圖處理用戶的請求並返回響應。
models.py:

位置: app資料夾內
用途: 定義資料庫的模型。每個模型通常映射到資料庫中的一個表。
admin.py:

位置: app資料夾內
用途: 定義Django的管理後台界面，可以定義如何顯示模型、自定義表單等。
apps.py:

位置: app資料夾內
用途: 包含app的配置類，可以設定app的名稱、標籤等。
tests.py:

位置: app資料夾內
用途: 包含針對app的測試代碼。
migrations/init.py:

位置: app資料夾下的 migrations 子資料夾內
用途: 讓 migrations 資料夾被識別為Python的模組。其他在此資料夾下生成的 .py 檔案通常是Django用於資料庫遷移的腳本。
forms.py (可選，但常見):

位置: app資料夾內
用途: 定義Django表單，可以是基於模型的表單或常規表單。
以上是一些常見的Django .py 檔案及其用途。根據你的專案和需求，可能還會有其他額外的 .py 檔案。



