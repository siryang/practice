
glTexParameter:纹理控制函数
GL_TEXTURE_MAG_FILTER // 放大滤波方式
GL_TEXTURE_MIN_FILTER // 缩小滤波方式

GL_NEAREST // 坐标最靠近象素中心的纹素
GL_LINEAR // 最靠近象素中心的四个象素的加权平均值

GL_TEXTURE_WRAP_S
GL_REPEAT
// 定义使用minmap时，纹理选择方法
// 纹理坐标超出(0,1)范围时，选择重复映射或者约简映射

glTexEnv:纹理颜色叠加方式

glTexGen:自动生成纹理坐标


``` 尝试一下这块代码能否读纹理内容
    // 读取像素
    glPixelStorei(GL_UNPACK_ALIGNMENT, 4);
    glReadPixels(0, 0, WindowWidth, WindowHeight, GL_RGB, GL_UNSIGNED_BYTE,pPixelData);
```


```
    glEnable(GL_BLEND);

    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE);
    glBlendFunc(GL_ONE, GL_ONE_MINUS_SRC_ALPHA);
    glEnable(GL_TEXTURE_2D);
    glEnableClientState(GL_VERTEX_ARRAY);
    glEnableClientState(GL_TEXTURE_COORD_ARRAY);

    // 绑定纹理对象
    glBindTexture(GL_TEXTURE_2D, textureId);

    glVertexPointer(2, GL_FLOAT, 0, vertexs);
    glTexCoordPointer(2, GL_FLOAT, 0, textures);
    glDrawArrays(GL_TRIANGLE_FAN, 0, 4);

    // 取消绑定纹理
    glBindTexture(GL_TEXTURE_2D, INVALID_TEXTUREID);
    glDisableClientState(GL_VERTEX_ARRAY);
    glDisableClientState(GL_TEXTURE_COORD_ARRAY);
    glDisable(GL_TEXTURE_2D);
```