from nonebot import on_command, CommandSession
import requests

# 签到URL
submit_url = ''  # 自行填写

#请求头
my_header={
    'user-agent': '' # 自行填写
}


# 数据信息
# 自行填写
json = {} # 格式为字典



# on_command 装饰器将函数声明为一个命令处理器
# 这里 sign_in 为命令的名字，同时允许使用别名「签到」「打卡」
@on_command('sign_in', aliases=('签到', '打卡'))
async def sign_in(session: CommandSession):
    # 从会话状态（session.state）中获取城市名称（name），如果当前不存在，则询问用户
    name = session.get('name', prompt='你想签到的名字？')
    # 获取签到的名字
    sign_in_state = await get_sign_in_state(name)
    # 向用户发送签到状态
    await session.send(sign_in_state)




# sign_in.args_parser 装饰器将函数声明为 sign_in 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@sign_in.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将名字跟在命令名后面，作为参数传入
            # 例如用户可能发送了：签到 xx
            session.state['name'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('要签到的姓名不能为空呢，请重新输入')

    # 如果当前正在向用户询问更多信息（例如本例中的要签到的名字），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg


async def get_sign_in_state(name: str) -> str:
    # 这里简单返回一个字符串
    # 自行修改
    re = requests.post(submit_url,json=json,headers=my_header)
    re.encoding=re.apparent_encoding
    if "不能重复回到同意问卷" in re.text :
        return f'{name}的签到状态是：已经签过了'
    if "提交成功" in re.text :
        return f'{name}的签到状态是：签到成功'

