```
#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;

void main() {
    vec2 st = gl_FragCoord.xy/u_resolution;
    float x = (st.x - 0.5) * (cos(u_time) * 2.0 + 5.0);
    float y = (st.y - 0.5) * 4.0;
    float t = x*x + y*y - 2.0 + sin(u_time) * 1.0;
    float v = t*t*t - y*y*y * x*x;
    gl_FragColor = vec4(v<0.0?1.0:0.0, 0.0, 0.0,1.0);
}
```