import xadmin
from .models import EmailCode
from xadmin import views


class EmailCodeAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    # search_fields 是为后台增加搜索功能
    search_fields = ['code', 'email', 'send_type']
    # list_filter 增加后台模型的搜索功能
    list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(EmailCode, EmailCodeAdmin)


class BaseSetting(object):
    """这里我们把Django后台的主题功能设置为True"""
    enable_themes = True
    use_bootswatch = True


# 我们用xadmin里面的views.BaseAdminView类进行注册
xadmin.site.register(views.BaseAdminView, BaseSetting)


# 这里对站点的标题以及页脚进行修改,以及总体
class GlobalSettings(object):
    site_title = '橙子后台管理系统'
    site_footer= '橙子之家'
    menu_style = 'accordion'


xadmin.site.register(views.CommAdminView, GlobalSettings)