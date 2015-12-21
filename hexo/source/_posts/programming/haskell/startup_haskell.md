

`ghci`
`runhaskell xxx.hs` or `runghc xxx.hs`
`#!/usr/bin/env runhaskell`


## Effective of Haskell

`div`, `mod`: -20 `divMod` 3 is (-7, 1) 向负无穷大对齐
`quot`, `rem`:  -20 `quotRem` 3 is (-6, -2) 向0对齐
quot要比div效率高一些，因为div对负数有特殊处理。

## Problem

* How to append element to list.