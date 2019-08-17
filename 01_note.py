#1.谈谈你对HTTP协议的认识。
#什么是协议？
#协议，是指通信的双方，在通信流程或内容格式上，共同遵守的标准。
#什么是http协议？
#http协议，是互联网中最常见的网络通信标准。
# http协议的特点
# ①通信流程：断开式（无状态）
# 断开式：http协议每次响应完成后，会断开与客户端的连接
# 无状态：由于服务器断开了之前的连接，就无法知晓连接间的关系
# ②内容格式：消息头和消息体
# 2）HTTP请求的方法：
# HTTP/1.1协议中共定义了八种方法（有时也叫“动作”），来表明Request-URL指定的资源不同的操作方式
# 1、OPTIONS
# 返回服务器针对特定资源所支持的HTTP请求方法，也可以利用向web服务器发送‘*’的请求来测试服务器的功能性
# 2、HEAD
# 向服务器索与GET请求相一致的响应，只不过响应体将不会被返回。这一方法可以再不必传输整个响应内容的情况下，就可以获取包含在响应小消息头中的元信息。
# 3、GET
# 向特定的资源发出请求。它本质就是发送一个请求来取得服务器上的某一资源。资源通过一组HTTP头和呈现数据（如HTML文本，或者图片或者视频等）返回给客户端。GET请求中，永远不会包含呈现数据。
# 4、POST
# 向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST请求可能会导致新的资源的建立和/或已有资源的修改。 Loadrunner中对应POST请求函数：web_submit_data,web_submit_form
# 5、PUT
# 向指定资源位置上传其最新内容
# 6、DELETE
# 请求服务器删除Request-URL所标识的资源
# 7、TRACE
# 回显服务器收到的请求，主要用于测试或诊断
# 8、CONNECT
# HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。
# 注意：
# 1）方法名称是区分大小写的，当某个请求所针对的资源不支持对应的请求方法的时候，服务器应当返回状态码405（Mothod Not Allowed）；当服务器不认识或者不支持对应的请求方法时，应返回状态码501（Not Implemented）。
# 2）HTTP服务器至少应该实现GET和HEAD/POST方法，其他方法都是可选的，此外除上述方法，特定的HTTP服务器支持扩展自定义的方法。
#
# 3.rest_framework 认证组件的流程
# django rest framework框架的认证流程
#1.用户请求走进来后,走APIView,初始化了默认的认证方法
#2.走到APIView的dispatch方法,initial方法调用了request.user
#3.如果我们配置了认证类,走我们自己认证类中的authentication方法
# 4.django  migrate 和makemigrations的差别
# python manger.py makemigrations
# 相当于 在该app下建立 migrations目录，并记录下你所有的关于modes.py的改动，比如0001_initial.py，
# 但是这个改动还没有作用到数据库文件
# python manager.py migrate
# 将该改动作用到数据库文件，比如产生table之类
# 5.说一下Django，MIDDLEWARES中间件的作用和应用场景？
#中间件是介于request与response处理之间的一道处理过程,用于在全局范围内改变Django的输入和输出。
#简单的来说中间件是帮助我们在视图函数执行之前和执行之后都可以做一些额外的操作
#例如：
#1.Django项目中默认启用了csrf保护,每次请求时通过CSRF中间件检查请求中是否有正确#token值
#2.当用户在页面上发送请求时，通过自定义的认证中间件，判断用户是否已经登陆，未登陆就去登陆。
#3.当有用户请求过来时，判断用户是否在白名单或者在黑名单里
# 6.使用orm和原生sql的优缺点？
#1.orm的开发速度快,操作简单。使开发更加对象化
#执行速度慢。处理多表联查等复杂操作时,ORM的语法会变得复杂
#2.sql开发速度慢,执行速度快。性能强



# 7.django中如何根据数据库表生成model中的类？
# 1.在settings中设置要连接的数据库
#2.生成model模型文件
#python manage.py inspectdb
#3.模型文件导入到models中
#    python manage.py inspectdb > app/models.py


# 8.谈谈你对restful规范的认识？
#首先restful是一种软件架构风格或者说是一种设计风格，并不是标准，它只是提供了一组设计#原则和约束条件，主要用于客户端和服务器交互类的软件。
#就像设计模式一样，并不是一定要遵循这些原则，而是基于这个风格设计的软件可以更简洁，更#有层次，我们可以根据开发的实际情况，做相应的改变。
#它里面提到了一些规范，例如：
#1.restful 提倡面向资源编程,在url接口中尽量要使用名词，不要使用动词
#2、在url接口中推荐使用Https协议，让网络接口更加安全
#https://www.bootcss.com/v1/mycss？page=3
#（Https是Http的安全版，即HTTP下加入SSL层，HTTPS的安全基础是SSL，
#因此加密的详细内容就需要SSL（安全套接层协议））
#3、在url中可以体现版本号
#https://v1.bootcss.com/mycss
#不同的版本可以有不同的接口，使其更加简洁，清晰
#4、url中可以体现是否是API接口
#https://www.bootcss.com/api/mycss
#5、url中可以添加条件去筛选匹配
#https://www.bootcss.com/v1/mycss？page=3
#6、可以根据Http不同的method，进行不同的资源操作
#（5种方法：GET / POST / PUT / DELETE / PATCH）
#7、响应式应该设置状态码
#8、有返回值，而且格式为统一的json格式
#9、返回错误信息
#返回值携带错误信息
#10、返回结果中要提供帮助链接，即API最好做到Hypermedia


# 9.django rest framework框架中都有那些组件？
#1.序列化组件:serializers  对queryset序列化以及对请求数据格式校验
#2.路由组件routers 进行路由分发
#3.视图组件ModelViewSet  帮助开发者提供了一些类，并在类中提供了多个方法
#4.认证组件 写一个类并注册到认证类(authentication_classes)，在类的的authticate方法中编写认证逻
#5.权限组件 写一个类并注册到权限类(permission_classes)，在类的的has_permission方法中编写认证逻辑。
#6.频率限制 写一个类并注册到频率类(throttle_classes)，在类的的allow_request/wait 方法中编写认证逻辑
#7.解析器  选择对数据解析的类，在解析器类中注册(parser_classes)
#8.渲染器 定义数据如何渲染到到页面上,在渲染器类中注册(renderer_classes)
#9.分页  对获取到的数据进行分页处理, pagination_class
#10.版本  版本控制用来在不同的客户端使用不同的行为
#在url中设置version参数，用户请求时候传入参数。在request.version中获取版本，根据版本不同 做不同处理


# 10.django rest framework如何实现的用户访问频率控制
#使用IP/用户账号作为键，每次的访问时间戳作为值，构造一个字典形式的数据，存起来，每次访问时对时间戳列表的元素进行判断，
#把超时的删掉，再计算列表剩余的元素数就能做到频率限制了
#匿名用户：使用IP控制，但是无法完全控制，因为用户可以换代理IP登录用户：使用账号控制，但是如果有很多账号，也无法限制
# 11.rest_framework序列化组件的作用,以及一些外键关系的钩子方法
#作用：帮助我们序列化数据
#1.choices  get_字段名_display
#2.ForeignKey source=orm 操作
#3.ManyToManyFiled  SerializerMethodField()
#                    def get_字段名():
#                    return 自定义
# 12.PV和UV
#1.pv:页面访问量,没打开一次页面PV计算+1,页面刷新也是
#2.UV：独立访问数,一台电脑终端为一个访客
# 13.cookie和session的区别
# HTTP被设计为”无状态”，每次请求都处于相同的空间中。 在一次请求和下一次请求之间没有任何状态保持，我们无法根据请求的任何方面(IP地址，用户代理等)来识别来自同一人的连续请求。上图很明显的展示了Django的session与cookie的实现原理。服务器会生成两份相同的cookie字符串，一份保存在本地，一份发向请求的浏览器。浏览器将收到的cookie字符串保存下来，当下次再发请求时，会将信息与这段cookie一同发送到服务器，服务器得到这段cookie会与本地保存的那份判断是否相同，如果相同就表示用户已经登录成功，保存用户登录成功的状态。Django的session保存在数据库中的数据相当于一个大字典，key为cookie的字符串，value仍是一个字典，字典的key和value为用户设置的相关信息。这样就可以方便的存取session里面的信息。
# Cookie概念
# ​ 在浏览某些 网站 时,这些网站会把 一些数据存在 客户端 , 用于使用网站 等跟踪用户,实现用户自定义 功能.
# 是否设置过期时间:
# 如果不设置 过期时间,则表示这个 Cookie生命周期为 浏览器会话期间 , 只要关闭浏览器,cookie就消失了.这个生命期为浏览会话期的cookie,就是会话Cookie;
# 存储:
# 一般保存在 内存,不在硬盘;如果设置了过期时间, 浏览器会把cookie保存在硬盘上,关闭再打开浏览器, 这些cookie 依然有效直到 超过的设置过期时间;存储在硬盘上的Cookie可以在不同的浏览器进程间共享，比如两个IE窗口。而对于保存 在内存的Cookie，不同的浏览器有不同的处理方式。
# Session概念
# 作用：实现网页之间数据传递，是一个存储在服务器端的对象集合。
# 原理：当用户请求一个Asp.net页面时，系统将自动创建一个Session;退出应用程序或关闭服务器时，该Session撤销。系统在创建Session时将为其分配一个长长的字符串标识，以实现对Session进行管理与跟踪。session机制是一种服务器端的机制，服务器使用一种类似于散列表的结构（也可能就是使用散列表）来保存信息。
#
# 保存:存储在Server段的内存进程中的，而这个进程相当不稳定，经常会重启，这样重启的话，就会造成Session失效，用户就必须要重新登录，用户体验相当差，比如用户在填写资料，快要结束的时候Session失效，直接跳到登录页面;
# 是否已经创建过session:
# 当程序需要为某个客户端的请求创建一个session时，服务器首先检查这个客户端的请求里是否已包含了一个session标识（称为session id），这个 ID 通常是 name为 JSESIONID 的一个 Cookie。
# 如果已包含则说明以前已经为此客户端创建过session，服务器就按照session id把这个session检索出来….使用（检索不到，会新建一个），
# 如果客户端请求不包含session id，则为此客户端创建一个session并且生成一个与此session相关联的session id，
# session id的值应该是一个既不会重复，又不容易被找到规律以仿造的字符串，这个session id将被在本次响应中返回给客户端保存。
# (总结: 创建一个session时,服务器看这个客户端 是否包含session标识, 是的话按照session id把session检索出来,否则就得 新建一个.)
# 区别：
# 1、cookie数据存放在客户的浏览器上，session数据放在服务器上.
# ​ 简单的说，当你登录一个网站的时候，如果web服务器端使用的是session,那么所有的数据都保存在服务器上面，客户端每次请求服务器的时候会发送 当前会话的session_id，服务器根据当前session_id判断相应的用户数据标志，以确定用户是否登录，或具有某种权限。
# Session是由应用服务器维持的一个服务器端的存储空间，用户在连接服务器时，会由服务器生成一个唯一的SessionID,用该SessionID 为标识符来存取服务器端的Session存储空间。而SessionID这一数据则是保存到客户端，用Cookie保存的，用户提交页面时，会将这一 SessionID提交到服务器端，来存取Session数据。这一过程，是不用开发人员干预的。所以一旦客户端禁用Cookie，那么Session也会失效。
# 2、cookie不是很安全，别人可以分析存放在本地的COOKIE并进行COOKIE欺骗考虑到安全应当使用session。
# 3、session会在一定时间内保存在服务器上。当访问增多，会比较占用你服务器的性能考虑到减轻服务器性能方面，应当使用COOKIE。
# 4、单个cookie保存的数据不能超过4K，很多浏览器都限制一个站点最多保存20个cookie。(Session对象没有对存储的数据量的限制，其中可以保存更为复杂的数据类型)
# 14.WSGI 和 uWSGI在django中的作用
# WSGI
# WSGI是一种WEB服务器  ==网关接口==。 是一个Web服务器（如nginx）与应用服务器（如uWSGI）通信的一种规范（协议）。
# 在生产环境中使用WSGI作为python web的服务器。Python Web服务器网关接口，是Python应用程序或框架和Web服务器之间的一种接口，被广泛接受。WSGI没有官方的实现, 因为WSGI更像一个协议，只要遵照这些协议，WSGI应用(Application)都可以在任何服务器(Server)上运行。
# uWSGI
# uWSGI实现了WSGI的所有接口，是一个快速、自我修复、开发人员和系统管理员友好的服务器。uWSGI代码完全用C编写，效率高、性能稳定。
# uwsgi是一种线路协议而不是通信协议，在此常用于在uWSGI服务器与其他网络服务器的数据通信。uwsgi协议是一个uWSGI服务器自有的协议，它用于定义传输信息的类型。
# 作用
# Django 是一个 Web 框架，框架的作用在于处理 request 和 reponse，其他的不是框架所关心的内容。所以怎么部署 Django 不是 Django 所需要关心的。
# Django 所提供的是一个开发服务器，这个开发服务器，没有经过安全测试，而且使用的是 Python 自带的 simple HTTPServer 创建的，在安全性和效率上都是不行的
# 而uWSGI 是一个全功能的 HTTP 服务器，他要做的就是把 HTTP 协议转化成语言支持的网络协议。比如把 HTTP 协议转化成 WSGI 协议，让 Python 可以直接使用。
# uwsgi 是一种 uWSGI 的内部协议，使用二进制方式和其他应用程序进行通信。
# 15.对Django的认识？
#1.Django是走大而全的方向，它最出名的是其全自动化的管理后台：只需要使用起ORM，做简单的对象定义，它就能自动生成数据库结构、以及全功能的管理后台。
#2.Django内置的ORM跟框架内的其他模块耦合程度高。
# 应用程序必须使用Django内置的ORM，否则就不能享受到框架内提供的种种基于其ORM的便利；
# 理论上可以切换掉其ORM模块，但这就相当于要把装修完毕的房子拆除重新装修，倒不如一开始就去毛胚房做全新的装修。
#3.Django的卖点是超高的开发效率，其性能扩展有限；采用Django的项目，在流量达到一定规模后，都需要对其进行重构，才能满足性能的要求。
#4.Django适用的是中小型的网站，或者是作为大型网站快速实现产品雏形的工具。
#5.Django模板的设计哲学是彻底的将代码、样式分离； Django从根本上杜绝在模板中进行编码、处理数据的可能。
# 16.Django 、Flask、Tornado的对比
#1.Django走的是大而全的方向,开发效率高。它的MTV框架,自带的ORM,admin后台管理,自带的sqlite数据库和开发测试用的服务器
#给开发者提高了超高的开发效率
#2.Flask是轻量级的框架,自由,灵活,可扩展性很强,核心基于Werkzeug WSGI工具和jinja2模板引擎
#3.Tornado走的是少而精的方向,性能优越。它最出名的是异步非阻塞的设计方式
#Tornado的两大核心模块：
#    1.iostraem：对非阻塞式的socket进行简单的封装
#    2.ioloop：对I/O多路复用的封装，它实现了一个单例
#17.协程
#18.django的缓存方式
#开发调试
#内存
#文件
#数据库
#Memcache缓存（python-memcached模块）
#Memcache缓存（pylibmc模块）
#应用
#1. 全站使用缓存
#使用中间件，经过一系列的认证等操作，如果内容在缓存中存在，则使用FetchFromCacheMiddleware获取内容并返回给用户，当返回给用户之前，判断缓存中是否已经存在，如果不存在则UpdateCacheMiddleware会将缓存保存至缓存，从而实现全站缓存

#MIDDLEWARE = [

# 'django.middleware.cache.UpdateCacheMiddleware',#放到第一个中间件位置

# 其他中间件...

#'django.middleware.cache.FetchFromCacheMiddleware',#放到最后一个

#]



#CACHE_MIDDLEWARE_ALIAS = ""

#CACHE_MIDDLEWARE_SECONDS = ""

#CACHE_MIDDLEWARE_KEY_PREFIX = ""

#2. 单独视图缓存

#方式一：装饰器

#from django.views.decorators.cache import cache_page



#@cache_page(60 * 15)

#def my_view(request):

#   ...

#<br>方式二：装饰器的另外一种写法

from django.views.decorators.cache import cache_page



#urlpatterns = [

#   url(r'^foo/([0-9]{1,2})/$', cache_page(60 * 15)(my_view)),

#]

#3. 局部视图缓存
#a. 引入TemplateTag

#{% load cache %}

#b. 使用缓存
#{% cache 5000 缓存key %} #这里是缓存5秒

#缓存内容

#{% endcache %}


# 由于Django构建得是动态网站，每次客户端请求都要严重依赖数据库，当程序访问量大时，耗时必然会更加明显，最简单解决方式是使用：
# 缓存，缓存将一个某个views的返回值保存至内存或者memcache中，5分钟内再有人来访问时，则不再去执行view中的操作，
# 而是直接从内存memcached 、Redis中之前缓存的内容拿到，并返回。