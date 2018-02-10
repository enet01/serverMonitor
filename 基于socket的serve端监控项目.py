#coding:utf-8
import psutil
import time
import socket
import os,sys
print "===========  系统当前用户:%s        ==============="%psutil.users()[0].name
print "===========  系统当前时间:%s  ==============="%time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
print
def mem():
    mem=psutil.virtual_memory()
    mem_list=[mem.total,mem.used,mem.free,mem.percent]
    return(mem_list)
   
def disk():
    disk_list=[psutil.disk_usage('/').total,psutil.disk_usage('/').used,psutil.disk_usage('/').free,psutil.disk_usage('/').percent]
    return disk_list
def net():
    net_list=[psutil.net_io_counters().bytes_sent, psutil.net_io_counters().bytes_recv, psutil.net_io_counters().packets_sent, psutil.net_io_counters().packets_recv]
    return net_list
def cpu():
    return ('cpu'+str(psutil.cpu_percent())+"%")
cpulist=cpu()
netlist=net()
memlist=mem()
disklist=disk()
print cpulist
print netlist
print memlist
print disklist

myfile = open(r'C:\Users\Administrator\Desktop\1.txt','w+')
myfile.write("系统当前用户:%s\n"%psutil.users()[0].name)
myfile.write("系统当前时间:%s\n"%time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
myfile.write("---------------------\n")
myfile.write("cpu使用率%s\n"%cpulist)
myfile.write("---------------------\n")
myfile.write("网络发送字节数:%sM\n"%(netlist[0]//1000000))
myfile.write("网络接收字节数:%sM\n"%(netlist[1]//1000000))
myfile.write("网络发送数据包:%sM\n"%(netlist[2]//1000000))
myfile.write("网络接收数据包:%sM\n"%(netlist[3]//1000000))
myfile.write("---------------------\n")
myfile.write("内存总数 :%sM\n"%(memlist[0]//1000000))
myfile.write("内存使用 :%sM\n"%(memlist[1]//1000000))
myfile.write("内存空闲 :%sM\n"%(memlist[2]//1000000))
myfile.write("内存使用率:%s\n"%(memlist[3]))
myfile.write("---------------------\n")
myfile.write("硬盘总数 :%sM\n"%(disklist[0]//1000000))
myfile.write("硬盘使用:%sM\n"%(disklist[1]//1000000))
myfile.write("硬盘空闲:%sM\n"%(disklist[2]//1000000))
myfile.write("硬盘使用率:%s\n"%(disklist[3]))
myfile.close()
f = open(r'C:\Users\Administrator\Desktop\1.txt','rb')
result= f.read()

def reader(path):
        con=os.popen('cat %s'%path)
        content=con.read()
        con.close()
        return content

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('192.168.0.6',8001))
while True:
    #kk=raw_input("peease input>>>>>")
    #sock.send(kk.encode('gbk'))
    
    canshu=sock.recv(2048)
#     result=reader(canshu)
    print(canshu)
    print(f)
    sock.send(result)   
    f.close()
    print("success")
sock.close()

 

------------------服务器端接收的结果：如下-----------------------------------

系统当前用户:Administrator
系统当前时间:2016-10-29 15:59:07
---------------------
cpu使用率cpu0.0%
---------------------
网络发送字节数:1389M
网络接收字节数:17301M
网络发送数据包:10M
网络接收数据包:0M
---------------------
内存总数 :12738M
内存使用 :5531M
内存空闲 :7206M
内存使用率:43.4
---------------------
硬盘总数 :107375M
硬盘使用:82750M
硬盘空闲:24625M
硬盘使用率:77.1

 

=================================用的的模块和函数==========================
https://pypi.python.org/pypi/psutil
#获取要监控的计算机的信息
   os.system   os.popen   /proc/file   字符串处理 \n   编码
#CPU
      #user time      #system  time      #wait IO 空闲时间      #idle百分比
      import psutil      psutil.cpu_times()              #所有核
      psutil.cpu_times(percpu=True)          #单核
      psutil.cpu_count()              #逻辑核数
      psutil.cpu_count(logical=False) #物理核数

#内存
    psutil.virtual_memory().total    psutil.virtual_memory().free    psutil.virtual_memory().available
    psutil.virtual_memory().cached    psutil.virtual_memory().used    psutil.virtual_memory().buffers
    psutil.virtual_memory().percent    psutil.swap_memory().total    psutil.swap_memory().used
    psutil.swap_memory().free    psutil.swap_memory().percent

  #磁盘
    psutil.disk_usage('/')    psutil.disk_io_counters()    psutil.disk_io_counters(perdisk=True)

  #进程
    psutil.pids()  #所有进程的pid    psutil.Process()  #进程对象
    psutil.Process(30708).name()  #进程名    psutil.Process(30708).exe()   #进程bin文件
    psutil.Process(30708).cwd()  #工作目录的绝对路径    psutil.Process(30708).status()  #进程状态
    psutil.Process(30708).create_time() #进程创建的时间戳 time.ctime(1476181891.27)
    psutil.Process(11092).uids() #进程所有者的用户id    psutil.Process(11092).gids() #进程所有者的组id
    psutil.Process(18202).cpu_times() #进程的CPU时间    psutil.Process(18202).memory_info() #
    psutil.Process(18202).io_counters() #进程的IO