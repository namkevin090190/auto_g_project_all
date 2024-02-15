# 1. Web Walkthrough
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->


## 1.1. What included in web
- Driver: selenium
- Approarch: POM - Page Object Model and Keyword driven



## 1.2. How to run
```
gauge run -e web/test
```

This will trigger the scenarios in `tests/examples/web` which is init a new driver for checking the visability of 2 buttons in google page.

## 1.3. How to implement new test

1. Create new package which represented for website in `platforms/web/pages/<website>` e.g. `kafka`
2. Create single page in package created in [1] e.g. `homepage.py`
3. Follow the structure defined in  `tests/examples/web`
   
# 2. Code Convention

## 2.1. Spec

```
    [Web][Website][PageName] step definition
```
*e.g. [Web][Kafka][Home] Click on search button*
## 2.2. Concept

### Definition
`Concept` is the group of steps which represent for single function.

### Where to place
`platforms/web/specs/concept`

*e.g. platforms/web/specs/concept/[Kafka] Search latest otp for <device_id>*

