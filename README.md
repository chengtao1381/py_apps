# py_apps
# redis 做缓存，支持复杂的数据结构，支持持久化，支持主从集群，支持高可用，支持较大的value 存储...
选redis 还是memcache
redis 分布式锁
redis 单线程结构，为何可以支持高并发
redis 主从结构

用redis 实现分布式锁，一台机器就存在单点问题。当master 挂掉的时候可以切换到slave。这又带来了新问题，由于redis 的复制是异步的，因此我们不能保证同时只有一个客户端获得锁。
一个显然的竞态条件：
1.Client A在master 上面成功获得了锁
2.master 在数据同步到slave 之前挂掉
3.slave 升级成为master
4.Client B申请了同样的资源的锁，成功了！
