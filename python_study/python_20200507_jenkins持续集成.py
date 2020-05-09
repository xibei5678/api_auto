#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20200507_jenkins持续集成.py
@Date  : 2020/5/7 0007 16:24
@Author: xibei
'''


'''jenkins 持续集成'''


'''下载安装'''
#  (a)、windows系统，直接下载安装包安装即可，安装完成后会自动启动服务，地址为：http:localhost：8080
#       默认端口号为8080，如果端口号被占用，可进入jenkins安装目录--jenkins.xml--找到“httpPort==8080'进行修改端口号
#  (b)、cetons系统安装


'''manage jenkins'''

# 1. Configure System (系统设置)
# （1）jenkins地址配置：manage jenkins--configure systm--jenkins location--jenkins URL:输入完成的ip地址
# （2）系统管理员邮箱配置：manage jenkins--configure systm--jenkins location-- e-mail address:输入邮箱地址

# 2. Configure Global Security（全局安全配置）
# 配置用户访问权限
# （1）Security Reaml:默认选 Jenkins’ ownf user database(jenkins 专有用户数据库)
# （2）Authorization（认证）：根据具体需求进行配置


''' 新建任务'''
# 1. 任务类型：自由风格的项目
#   maven项目：开发用的多
#   流水线：工作流，开发测试一整套构建流程

# 2. workspace （工作空间--未进行项目的任何配置情况下）
#   a、发现jenkins安装目录下有一个workspace文件夹
#   b、直接将源码拷贝到workspace文件下
#   c、尝试构建：项目设置--build--Exectue Windows batch command(windows批处理命令)--” python run_test.py"
#      注意：1. Python 如果有多个版本 也需要详细路径
#         2.run_test文件的路径应为相对workspace的详细地址
#   d、进行构建，可直接进行构建


'''源码配置_非本地情况'''
# 1. 路径：任务配置--Source Code Managemnet--git/svn
# 2.git地址配置
# 3.Credentials：添加凭证（添加git的用户名密码）
# 4.保存
# 5.构建


''' 测试报告的配置 '''

# 1. 路径：任务配置--Post-build Actions--Add post-build action--选择“Publish HTML reports”
# 2.  添加html reports：
#      a.HTML directory to archive :输入html reports的获取路径/文件夹名（相对workspace）
#      b. index page[s]: 输入要获取的html reports文件的名字（如 auto_api_report.html）
#      c. Report title : 输入报告的标题
# 3. 保存后，再次构建。构建完成后，会展示html report。注意默认每次构建后，只显示最新一次的报告。
# 4. report 格式丢失：进入Manage Jenkins-> Script console，输入如下命令并进行执行。
#                   System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "")
# 5. 保存每次构建后的测试报告：在Publish HTML reports 添加时，--展开 publishing options-- 勾选 keep past HTML reports



''' 邮件配置_拓展版邮件配置'''

#  1.在jenkins 的系统配置里，先进行邮件发送的全局的配置
# (1)、操作路径： Manage Jenkins-- Configure System -- Extendde E-mail Notifiction
# (2)、配置项：
#      SMTP server: 输入发送邮件服务器（如果用qq邮箱即输入smtp.qq.com）
#      Default user E-mail suffix -- Advanced..:配置发送邮件的用户名密码
#           a. 勾选“Use SMTP Authentication”
#           b. 输入邮箱和密码
#               注意：1.输入的邮箱必须与上面“	System Admin e-mail address” 配置邮箱保持一致
#                    2.以qq邮箱为例，需保证qq邮箱已开启smtp服务(服务开启--设置--帐户--pops/smtp开启)
#                    3.输入的密码即为qq邮箱开启服务时的密码
#           c. 勾选 Use SSL
#           d. SMTP port: 端口号，qq为465
#           e. Charset : UTF-8
#      Default Content Type: 默认内容格式，选择html
#      Default Recipients：默认收件人，可配置自己的邮箱地址

# 2. 任务中的配置
# (1)、操作路径：Configure--Post-build Actions--Add post-build action--选择“Editable Email Notification”
# (2)、配置项：
#       Project Recipient List：收件人清单，$DEFAULT_RECIPIENTS 为全局设置中的收件人变量（可不做修改）
#       Project Reply-To List：回复人，$DEFAULT_REPLYTO 为全局设置中的回复人变量（可不做修改）
#       Content Type：邮件内容形式，选择Both HTML and Plain Text
#       Default Subject：输入邮件的主题
#       Default Content：输入邮件默认的内容
#       Attachments：添加附件，如添加测试报告，直接输入report相对workspace中的路径

#  （3）、设置触发邮件发送
#       a. 邮件触发默认为：构建失败才发送
#       b.设置触发: 点击高级设置advanced Settings-- Triggers--删除原有的“Failure-Any”--Add Trigger--根据需要添加tiggers，添加后再进行配置收件人
#
#

''' 持续构建_build triggers'''

# 1. build periodically 定时构建：设置时间，进行构建。如每天的几点进行构建job
#
# 2. Poll SCM 轮询构建：只要提交代码到git或svn，即自动构建job

# 3. 以上两种可以同时选择，不冲突