# Cocos2D

### 多线程
Cocos2d-x 的调度是纯粹的串行机制，
因此所有函数都运行在同一个线程，
不会存在并行程序的种种麻烦，
这大大简化了编程的复杂性。

### class CCSprite : CCNode

#### 节点树
* `addChild(CCNode* child);`                    增加子节点
* `removeChildByTag(int tag, bool cleanup);`    根据TAG删除节点
* `removeFromParentAndCleanup(bool cleanup);`   从父节点移除此Node，并根据cleanup参数调用cleanup函数。
* `getChildByTag(int tag);`
* `cleanup();`

#### 其它属性
* `CCActionManager* ActionManager;` 动作管理器
* `CCGLProgram* ShaderProgram;`     Shader程序
* `CCScheduler* Scheduler;`         定时器管理器
* `float SkewX; float SkewY;        斜切角度，用于沿X/Y轴翻转指定角度


### 定时器
#### update 定时器
每帧绘制之前都会被触发一次。

#### schedule 定时器
以一定的时间间隔连续调用某个函数。
Cocos2D中要求时间间隔必须大于两帧的间隔。否则两帧期间的多次调用实际会被合并。
每个Node可以有多个schedule.
``` c++
this->schedule(schedule_selector(GameScene::updateGame));
// GameScene::updateGame 是需要定时调用的函数。
// GameScene::updateGame 需要一个float参数，代表距前一次触发的时间间隔。
// schedule_selector是一个将函数转换为函数指针的宏。用的是static_cast<>
// schedule有不同的重载函数，可以指定`触发间隔`和`延时`。
```

* `schedule(SEL_SCHEDULE selector, float interval, unsigned int repeat, float delay);`
repeat 代表事件触发一次后，还会再次触发的次数，默认为无穷多次。






