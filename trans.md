*交接* by 周李峰(性质篇)
=======================

#目标
  本文档最终目的是实现顺利交接.  
just for ...

#内部
  本部分包括:开发环境,测试环境,预发环境,线上环境,SVN/MAVEN等杂项共5个部分  
具体见下面段落.
##1.Dev
  test2是面向开发的简单环境,包括3台机器  
    1.app16:数据库,部分中间件,详见*本地测试环境部署一览表.xlsx*  
    2.app17:基础应用,详见*本地测试环境部署一览表.xlsx*   
    3.app18:功能应用,详见*本地测试环境部署一览表.xlsx*

##2.Test
  test3是面向开发的环境,包括6台机器  
    1.app12:数据库1,部分中间件,详见*本地测试环境test3变更表.xlsx*  
    2.app13:基础应用,部分中间件,详见*本地测试环境test3变更表.xlsx*  
    3.app14:基础应用,部分中间件,详见*本地测试环境test3变更表.xlsx*  
    4.app15:功能应用,部分中间件,详见*本地测试环境test3变更表.xlsx*  
    5.app19:功能应用,部分中间件,详见*本地测试环境test3变更表.xlsx*  
    6.app20:数据库2,部分中间件,详见*本地测试环境test3变更表.xlsx*  


##3.PRE
  PRE是作为预发环境,包括5台机器  
    1.eln114:入口环境,部分中间件,详见*ELN4.0预发环境服务器部署计划.xlsx*  
    2.eln115:数据库,部分中间件,详见*ELN4.0预发环境服务器部署计划.xlsx*
    3.eln116:基础功能应用,部分中间件,数据库,详见*ELN4.0预发环境服务器部署计划.xlsx*
    4.eln117:基础功能应用,部分中间件,报表库,详见*ELN4.0预发环境服务器部署计划.xlsx*
    5.eln124:是从线上系统替换下来的应用服务器,有针对的部署新应用,部分中间件,详见*ELN4.0预发环境服务器部署计划.xlsx*

##4.PUB 
  详情：见(主机篇)

##5.SVN/MAVEN
  SVN和MAVEN在一台主机上  
    1.主机app11:作为SVN和MAVEN联系着所有代码和文档(公司)  
    2.svn1:在/web/svn/repos  
    3.svn2:在/web/svn/repos2  
    4.MAVEN在 [MAVEN](http://192.168.0.211:8080/nexus/index.html) 可以进行查询代码下载。  

##6.SQLITE
  SQLITE主要用报表(rfs)应用服务,具体安装过程也可参见<b style=color:blue>*外部*</b>-</b>*<b style=color:blue>InstallDoc</b>*-<b style=color:blue>SQLITE</b>部分 

##7.Slony
  Slony在只应用于线上和预发两套系统，只为(rfs)应用提供从主库到备库的拷贝.  
    + 安装步骤  
    1.`tar -xvf slony1-2.2.0.b5.tar.bz2`  
    2.`./configure --with-pgconfigdir=/opt/pgsql924/bin/`  
    3.`make && make install`  
    + 配置slony.(具体目录需要经过调整)   
    1.单个slony目录结构: drop_cluster_app.sh  init_app.sh  master_app.slon  slave_app.slon  
    2.init_app.sh 修改[SLONIK] , [MASTER_*] , [MASTER_DBNAME] , [SLAVE1*] 成对应的值.  
       set add table 里面配置所有需要同步的表.   
    3.master_app.slon 与slave_app.slon 里面修改 [cluster_name] 和 [conn_info] 成对应的值.  
    4.确认主库和从库(集群)里面是否有 无用的schema(例如:_report),有则删除.  
    5.执行 `sh init_app.sh` (经测试,pg9.2的执行需要nohup 后台执行)  
    6.`/web/pgsql/bin/slon -p /web/slony/report/uc/master_uc.slon.pid -f /web/slony/report/uc/master_uc.slon >>/web/slony/report/uc/master_uc.slon.log &`  
    `/web/pgsql/bin/slon -p /web/slony/report/uc/slave_uc.slon.pid -f /web/slony/report/uc/slave_uc.slon >>/web/slony/report/uc/slave_uc.slon.log &`  
    7.检查日志. 直到出来  
    `2014-02-10 17:10:52 CSTINFO   remoteWorkerThread_1: syncing set 1 with 21 table(s) from provider 1`    
    `2014-02-10 17:10:52 CSTINFO   remoteWorkerThread_1: SYNC 5004021843 done in 0.046 seconds`  

##8.PostgreSQL
  数据库的安装日常操作文档略过,已经融入到日常工作当中.  
    定时脚本,备份,全部参考(主机篇)

#外部
  本部分包括本人直接部署的两套环境(360BUF和YUTONG)和接手的1套环境(ZYD.CN)和一份不完整部署文档.  
  三个独立平台全为独立全功能买断！
##1.360BUY 
  JD商城学习系统是一套完全内网的独立环境,操作较为麻烦,领导是王工,人略好,京东大学的老师也不错.  
    1.京东升级后续工作人:杨洋[定制部]  
    2.学习系统部署情况表,请稳步[google-drive](https://docs.google.com/spreadsheet/ccc?key=0AjAdLLN_zTf5dC10WFp4Tm96bFRXSnpPb2gyQ0ctUHc&usp=sharing)  
    3.安装文档,请稳步[google-drive](https://docs.google.com/document/d/1YJwJctkrqIq4llhz_s3zbZj6KkhXqnQjj9XxHSQ9S1A/edit?usp=sharing)  
##2.YUTONG
  YUTONG客车在线学习系统能够外网操作,领导是顾老师,人略相当好.  
    1.宇通升级后续跟进人员:李翔[定制部]  
    2.鉴于当初项目进度原因部署详情表,请向跟进人员确认.本人暂无.    

##3.ZYD.CN
  此环境为交接环境,详情见:223(下面有介绍)主机的/home/doom/share/sdgh/doom/zyd  
    1.此环境也可与岳勇霞沟通.  

##4.InstallDoc
  安装文档,请稳步[google-drive](https://docs.google.com/document/d/1YJwJctkrqIq4llhz_s3zbZj6KkhXqnQjj9XxHSQ9S1A/edit?usp=sharing)  

#工作环境
  本部分包括工作主机,部署工具,简易脚本,文件传输,简易监控

##1.工作主机
  总共有两台分别是192.168.0.170(虚拟机不用关机,以下称170)互192.168.0.223(实体机可关机,以下称223) 他们的是互为备份的关系.    
    具体使用:2013-2-11到2013-3-7平常使用交流.

##2.部署工具(shell版)
  部署工具为最初Ant的改版(初始版)
    1.部署工具位于本地测试环境的/web/eln4share/test/new目录下,一般挂载到  
170或者223进行部署
    2.部署工具依赖key的验证(so:170,223到本地环境都是无密码验证的.)  
    3.部署时请su - web帐号.  
    4.具体用法:  
    <span style=color:red>`zlfcycle</span> *environment* *app-code* *action*`  
    environment:2 = test2 , 3 = test3 , pre = 预发  
    app-code: els-web,els-svc,rfs-svc (用英文半角逗号分割)  
    action: 1 = restart , 2 = start , 3 = shutdown , 4 = statuscheck , 6 = autodeploy     


##3.简易监控
  请点击[监控](yufa.21tb.com:8888/nagios) username:nagios password:******

##4.文件传输
  170已在公司出口网关端口转发(为6333端口) e.g.:scp -P 6333 1.md root@proxy:/tmp
