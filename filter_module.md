





<!DOCTYPE html>

<html lang="zh-CN">

<meta http-equiv="Content-Type" content="text/html; charset=utf-8">

<meta name="renderer" content="webkit" />

<meta name="format-detection" content="telephone=no">

<meta http-equiv="X-UA-Compatible" content="IE=edge,Chrome=1" />

<meta name="viewport" content="width=device-width, initial-scale=0.1" />

<meta http-equiv="Pragma" content="no-cache" />

<meta http-equiv="Cache-Control" content="no-cache" />

<meta http-equiv="Expires" content="0" />









<head>

&#x20;   <title>选课</title>

&#x20;   <link rel="stylesheet" href="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/css/bhTip.css?av=1781150761398">

&#x20;   <link rel="stylesheet" href="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/css/grablessons/grablessons.css?av=1781150761398">

&#x20;   <link rel="stylesheet" href="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/css/curriculavariable/bhwindow.css?av=1781150761398">

&#x20;   <link rel="stylesheet" href="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/css/curriculavariable/jqxTabs.css?av=1781150761398">

&#x20;   <link rel="stylesheet" href="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/css/electiveBatchAndXz.css?av=1781150761398">

&#x20;   <link rel="stylesheet" href="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/css/messageQueueTable.css?av=1781150761398">

</head>

<body>

&#x09;<div class="main">

&#x20;       <!--头部-->

&#x20;       <header class="cv-page-header cv-bg-color-primary cv-clearfix-child">

&#x20;           <!--logo-->

&#x20;           <img title="返回主页" src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/images/index/logo-mini2.png?av=1781150761398" id="cv-log-img">



&#x20;           <!--选课类型tab-->

&#x20;           <div class="cv-pull-left" cv-role="tabs">

&#x20;               <ul id="cvPageHeadTab" class="cv-tabs" cv-role="tabList">

&#x20;               </ul>

&#x20;           </div>

&#x20;           <nav>

&#x20;               <span id="goHome">返回主页</span>

&#x20;               <span id="logout">退出</span>

&#x20;           </nav>

&#x20;       </header>

&#x20;     

&#x20;       <!--推荐选课模块-->

&#x20;       <article id="cvRecommendCourse" class="cv-block-hide cv-pb-38">

&#x20;           <header class="cv-course-header cv-clearfix-child">

&#x20;               <div class="">

&#x20;                   <!-- <h3 class="cv-mb-8" id="recommendTitle">推荐选课</h3> -->

&#x20;                   <span class="cv-caption-text" id="recommendSpan"></span>

&#x20;                   <span class="credits">

&#x20;                   	<span class="credit-label" data-i18n-text="bxqzgxkxf">本学期最高选课学分</span>：

&#x20;                   	<span class="max-credit-value"></span>

&#x20;                   	<span class="credit-label" data-i18n-text="bxqzgxkxf">本学期已选学分</span>：

&#x20;                   	<span class="selected-credit-value"></span>

&#x20;                   </span>

&#x20;                   <div style="padding-top:5px;padding-bottom:5px">

&#x20;                       <label data-i18n-text="isConflict">是否冲突</label>: 

&#x20;                       <select class="cv-search-input search\_sfct" id="recommend\_sfct" courseType="TJKC">

&#x20;                           <option value="2" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                           <option value="1" data-i18n-text="isConflict">冲突</option>

&#x20;                           <option value="0" data-i18n-text="noConflict">不冲突</option>

&#x20;                       </select>

&#x20;                       <label data-i18n-text="isFull" >是否已满</label>: 

&#x20;                       <select class="cv-search-input search\_sfym" id="recommend\_sfym" courseType="TJKC">

&#x20;                           <option value="2" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                           <option value="1"  data-i18n-text="full">已满</option>

&#x20;                           <option value="0"  data-i18n-text="empty">未满</option>

&#x20;                       </select>   

&#x20;                       <label data-i18n-text="query.kcxz">课程性质</label>: 

&#x20;                       <select class="cv-search-input search\_kcxz" id="recommend\_kcxz" courseType="TJKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select>

&#x20;                       <label class="search\_kclb\_label" data-i18n-text="kclb">课程类别</label>: 

&#x20;                       <select class="cv-search-input search\_kclb" id="recommend\_kclb" courseType="TJKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select> 

&#x20;                       <input id="programSearch" class="cv-search-input cv-search-input-key" data-i18n-placeholder="query.placeholder2" placeholder="请输入课程名称/上课教师/课程编号/班号" type="text" courseType="FANKC"/>

&#x20;                   </div>

&#x20;               </div>

&#x20;               

&#x20;           </header>



&#x20;           <!--专家模式模块-->

&#x20;           <div id="cvExpertMode" class="cv-expert-mode">

&#x20;               <div id="cvCanSelectRecommendCourse" class="cv-tab-pane cv-active"></div>

&#x20;           </div>

&#x20;       </article>



&#x20;       <!-- 方案内课程模块 -->

&#x20;       <article id="cvProgramCourse" class="cv-block-hide cv-pb-38">

&#x20;           <header class="cv-course-header cv-clearfix-child">

&#x20;               <div>

&#x20;                   <div class="">

&#x20;                       <!-- <h3 class="cv-mb-8" id="programTitle">方案内选课</h3> -->

&#x20;                       <span class="cv-caption-text" id="programSpan"></span>

&#x20;                       <span class="credits">

&#x09;                    	<span class="credit-label" data-i18n-text="bxqzgxkxf">本学期最高选课学分</span>: 

&#x09;                    	<span class="max-credit-value"></span>

&#x09;                    	<span class="credit-label" data-i18n-text="bxqzgxkxf">本学期已选学分</span>: 

&#x09;                    	<span class="selected-credit-value"></span>

&#x09;                    </span>

&#x20;                       <div style="padding-top:5px;padding-bottom:5px">

&#x20;                           <label data-i18n-text="isConflict">是否冲突</label>: 

&#x20;                           <select class="cv-search-input search\_sfct" id="program\_sfct" courseType="FANKC">

&#x20;                               <option value="2" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                               <option value="1" data-i18n-text="isConflict">冲突</option>

&#x20;                               <option value="0" data-i18n-text="noConflict">不冲突</option>

&#x20;                           </select>

&#x20;                           <label data-i18n-text="isFull" >是否已满</label>: 

&#x20;                           <select class="cv-search-input search\_sfym" id="program\_sfym" courseType="FANKC">

&#x20;                               <option value="2" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                               <option value="1"  data-i18n-text="full">已满</option>

&#x20;                               <option value="0"  data-i18n-text="empty">未满</option>

&#x20;                           </select>   

&#x20;                           <label data-i18n-text="query.kcxz">课程性质</label>: 

&#x20;                           <select class="cv-search-input search\_kcxz" id="program\_kcxz" courseType="FANKC">

&#x20;                               <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                           </select>

&#x20;                           <label class="search\_kclb\_label" data-i18n-text="kclb">课程类别</label>: 

&#x20;                           <select class="cv-search-input search\_kclb" id="program\_kclb" courseType="FANKC">

&#x20;                               <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                           </select> 

&#x20;                           <input id="programSearch" class="cv-search-input cv-search-input-key" data-i18n-placeholder="query.placeholder2" placeholder="请输入课程名称/上课教师/课程编号/班号" type="text" courseType="FANKC"/>

&#x20;                       </div>

&#x20;                   </div>

&#x20;                   

&#x20;               </div>                       

&#x20;           </header>

&#x20;           

&#x20;           <div id="cvProgramExpertMode" class="cv-expert-mode">

&#x20;               <div id="cvCanSelectProgramCourse" class="cv-tab-pane cv-active"></div>

&#x20;           </div>

&#x20;       </article>



&#x20;       <!-- 方案外课程模块 -->

&#x20;       <article id="cvUnProgramCourse" class="cv-block-hide cv-pb-38">

&#x20;           <header class="cv-course-header cv-clearfix-child">

&#x20;               <div class="">

&#x20;                   <!-- <h3 class="cv-mb-8" id="unProgramTitle">方案外选课</h3> -->

&#x20;                   <span class="cv-caption-text" id="unProgramSpan"></span>

&#x20;                   <span class="credits">

&#x20;                   	<span class="credit-label" data-i18n-text="bxqzgxkxf">本学期最高选课学分</span>: 

&#x20;                   	<span class="max-credit-value"></span>

&#x20;                   	<span class="credit-label" data-i18n-text="bxqzgxkxf">本学期已选学分</span>: 

&#x20;                   	<span class="selected-credit-value"></span>

&#x20;                   </span>

&#x20;                   <div style="padding-top:5px;">

&#x20;                       <label data-i18n-text="isConflict">是否冲突</label>: 

&#x20;                       <select class="cv-search-input search\_sfct" id="unprogram\_sfct" courseType="FAWKC">

&#x20;                           <option value="2" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                           <option value="1" data-i18n-text="isConflict">冲突</option>

&#x20;                           <option value="0" data-i18n-text="noConflict">不冲突</option>

&#x20;                       </select>

&#x20;                       <label data-i18n-text="isFull" >是否已满</label>: 

&#x20;                       <select class="cv-search-input search\_sfym" id="unprogram\_sfym" courseType="FAWKC">

&#x20;                           <option value="2" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                           <option value="1"  data-i18n-text="full">已满</option>

&#x20;                           <option value="0"  data-i18n-text="empty">未满</option>

&#x20;                       </select>   

&#x20;                       <label data-i18n-text="query.kcxz">课程性质</label>: 

&#x20;                       <select class="cv-search-input search\_kcxz" id="unprogram\_kcxz" courseType="FAWKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select>

&#x20;                       <label class="search\_kclb\_label" data-i18n-text="kclb">课程类别</label>: 

&#x20;                       <select class="cv-search-input search\_kclb" id="unprogram\_kclb" courseType="FAWKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select> 

&#x20;                       <input id="unProgramSearch" class="cv-search-input cv-search-input-key" data-i18n-placeholder="query.placeholder2" placeholder="请输入课程名称/上课教师/课程编号/班号" type="text" courseType="FAWKC"/>

&#x20;                   </div>

&#x20;                   <div class="cv-minor-sknjyxzy">

&#x20;                       <label data-i18n-text="query.nj">上课年级</label>: 

&#x20;                       <select class="cv-search-input search\_nj" id="unprogram\_nj" courseType="FAWKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select>

&#x20;                       <label data-i18n-text="query.yx">上课院系</label>: 

&#x20;                       <select class="cv-search-input search\_yx" id="unprogram\_yx" courseType="FAWKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select>

&#x20;                       <label data-i18n-text="query.zy">上课专业</label>: 

&#x20;                       <select class="cv-search-input search\_zy" id="unprogram\_zy" courseType="FAWKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select>

&#x20;                   </div>

&#x20;               </div>  

&#x20;               

&#x20;           </header>



&#x20;           <div id="cvUnProgramExpertMode" class="cv-expert-mode">

&#x20;               <div id="cvCanSelectUnProgramCourse" class="cv-tab-pane cv-active"></div>

&#x20;           </div>

&#x20;       </article>



&#x20;       <!--公选课模块-->

&#x20;       <article id="cvPublicCourse" class="cv-block-hide cv-pb-38">

&#x20;           <!--头部-->

&#x20;           <header class="cv-course-header cv-clearfix-child">

&#x20;               <div class="">

&#x20;                   <!--标题-->

&#x20;                   <!-- <h3 class="cv-mb-8" id="publicTitle">公选课</h3> -->

&#x20;                   <!--说明-->

&#x20;                   <span class="cv-caption-text" id="publicSpan"></span>

&#x20;                   <span class="credits">

&#x20;                   	<span class="credit-label" data-i18n-text="bxqzgxkxf">本学期最高选课学分</span>: 

&#x20;                   	<span class="max-credit-value"></span>

&#x20;                   	<span class="credit-label" data-i18n-text="bxqzgxkxf">本学期已选学分</span>: 

&#x20;                   	<span class="selected-credit-value"></span>

&#x20;                   </span>

&#x20;                   <div style="padding-top:5px;padding-bottom:5px">

&#x20;                       <label data-i18n-text="isConflict">是否冲突</label>: 

&#x20;                       <select class="cv-search-input search\_sfct" id="public\_sfct" courseType="XGXK">

&#x20;                           <option value="2" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                           <option value="1" data-i18n-text="isConflict">冲突</option>

&#x20;                           <option value="0" data-i18n-text="noConflict">不冲突</option>

&#x20;                       </select>

&#x20;                       <label data-i18n-text="isFull" >是否已满</label>: 

&#x20;                       <select class="cv-search-input search\_sfym" id="public\_sfym" courseType="XGXK">

&#x20;                           <option value="2" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                           <option value="1"  data-i18n-text="full">已满</option>

&#x20;                           <option value="0"  data-i18n-text="empty">未满</option>

&#x20;                       </select>   

&#x20;                       <label class="search\_xgxklb\_label" data-i18n-text="xgxklb">通识课类别</label>: 

&#x20;                       <select class="cv-search-input search\_xgxklb" id="public\_xgxklb" courseType="XGXK">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select>

&#x20;                       <label id="course\_label" data-i18n-text="kcbk">课程板块</label>: 

&#x20;                       <select class="cv-search-input search\_course\_section" id="course\_section" courseType="XGXK">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select>

&#x20;                       <input id="publicSearch" class="cv-search-input cv-search-input-key" data-i18n-placeholder="query.placeholder2" placeholder="请输入课程名称/上课教师/课程编号/班号" type="text" courseType="XGXK"/>

&#x20;                   </div>

&#x20;               </div>

&#x20;               

&#x20;           </header>



&#x20;           <!--公共课列表-->

&#x20;           <div class="cv-public-course" cv-role="tabs">

&#x20;               <div id="cvCanSelectPublicCourse" class="cv-tab-pane cv-active"></div>

&#x20;           </div>

&#x20;       </article>



&#x20;       <!-- 重修模块 -->

&#x20;       <article id="cvRetakeCourse" class="cv-block-hide cv-pb-38">

&#x20;           <!--头部-->

&#x20;           <header class="cv-course-header cv-clearfix-child">

&#x20;               <div class="">

&#x20;                   <!--标题-->

&#x20;                   <!-- <h3 class="cv-mb-8" id="retakeTitle">重修选课</h3> -->

&#x20;                   <!--说明-->

&#x20;                   <span class="cv-caption-text" id="retakeSpan"></span>

&#x20;                   <span class="credits">

&#x20;                   	<span class="credit-label" data-i18n-text="bxqzgxkxf">本学期最高选课学分</span>：

&#x20;                   	<span class="max-credit-value"></span>

&#x20;                   	<span class="credit-label" data-i18n-text="bxqzgxkxf">本学期已选学分</span>：

&#x20;                   	<span class="selected-credit-value"></span>

&#x20;                   </span>

&#x20;                   <div style="padding-top:5px;padding-bottom:5px">

&#x20;                       <label data-i18n-text="isConflict">是否冲突</label>：

&#x20;                       <select class="cv-search-input search\_sfct" id="retake\_sfct" courseType="CXKC">

&#x20;                           <option value="2" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                           <option value="1" data-i18n-text="isConflict">冲突</option>

&#x20;                           <option value="0" data-i18n-text="noConflict">不冲突</option>

&#x20;                       </select>

&#x20;                       <label data-i18n-text="isFull" >是否已满 </label>：

&#x20;                       <select class="cv-search-input search\_sfym" id="retake\_sfym" courseType="CXKC">

&#x20;                           <option value="2" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                           <option value="1"  data-i18n-text="full">已满</option>

&#x20;                           <option value="0"  data-i18n-text="empty">未满</option>

&#x20;                       </select>   

&#x20;                       <label data-i18n-text="query.kcxz">课程性质</label>：

&#x20;                       <select class="cv-search-input search\_kcxz" id="retake\_kcxz" courseType="CXKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select>

&#x20;                       <label class="search\_xklx\_label" data-i18n-text="query.cxlx">选课类型</label>：

&#x20;                       <select class="cv-search-input search\_xklx" id="retake\_xklx" courseType="CXKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                           <option value="1" data-i18n-text="query.cxlx1">缓考首修</option>

&#x20;                           <option value="2" data-i18n-text="query.cxlx2">重修</option>

&#x20;                       </select>

&#x20;                       <label class="search\_kclb\_label" data-i18n-text="kclb">课程类别</label>：

&#x20;                       <select class="cv-search-input search\_kclb" id="retake\_kclb" courseType="CXKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select>

&#x20;                       <input id="retakeSearch" class="cv-search-input cv-search-input-key" data-i18n-placeholder="query.placeholder2" placeholder="请输入课程名称/上课教师/课程编号/班号" type="text" courseType="CXKC"/>

&#x20;                   </div>

&#x20;               </div>

&#x20;               

&#x20;           </header>



&#x20;           <!--重修课列表-->

&#x20;           <div class="cv-public-course" cv-role="tabs">

&#x20;               <div id="cvCanSelectRetakeCourse" class="cv-tab-pane cv-active"></div>

&#x20;           </div>

&#x20;       </article>



&#x20;       <!-- 体育课模块 -->

&#x20;       <article id="cvSportCourse" class="cv-block-hide cv-pb-38">

&#x20;           <!--头部-->

&#x20;           <header class="cv-course-header cv-clearfix-child">

&#x20;               <div class="">

&#x20;                   <!--标题-->

&#x20;                   <!-- <h3 class="cv-mb-8" id="sportTitle">体育选课</h3> -->

&#x20;                   <!--说明-->

&#x20;                   <span class="cv-caption-text" id="sportSpan"></span>

&#x20;                   <span class="credits">

&#x20;                   	<span class="credit-label" data-i18n-text="bxqzgxkxf">本学期最高选课学分</span>：

&#x20;                   	<span class="max-credit-value"></span>

&#x20;                   	<span class="credit-label" data-i18n-text="bxqzgxkxf">本学期已选学分</span>：

&#x20;                   	<span class="selected-credit-value"></span>

&#x20;                   </span>

&#x20;                   <div style="padding-top:5px;padding-bottom:5px">

&#x20;                       <label data-i18n-text="isConflict">是否冲突</label>：

&#x20;                       <select class="cv-search-input search\_sfct" id="sport\_sfct" courseType="TYKC">

&#x20;                           <option value="2" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                           <option value="1" data-i18n-text="isConflict">冲突</option>

&#x20;                           <option value="0" data-i18n-text="noConflict">不冲突</option>

&#x20;                       </select>

&#x20;                       <label data-i18n-text="isFull" >是否已满</label>：

&#x20;                       <select class="cv-search-input search\_sfym" id="sport\_sfym" courseType="TYKC">

&#x20;                           <option value="2" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                           <option value="1"  data-i18n-text="full">已满</option>

&#x20;                           <option value="0"  data-i18n-text="empty">未满</option>

&#x20;                       </select>   

&#x20;                       <label data-i18n-text="query.kcxz">课程性质</label>：

&#x20;                       <select class="cv-search-input search\_kcxz" id="sport\_kcxz" courseType="TYKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select>

&#x20;                       <label class="search\_kclb\_label" data-i18n-text="kclb">课程类别</label>：

&#x20;                       <select class="cv-search-input search\_kclb" id="sport\_kclb" courseType="TYKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select> 

&#x20;                        <input id="sportSearch" class="cv-search-input cv-search-input-key" data-i18n-placeholder="query.placeholder2" placeholder="请输入课程名称/上课教师/课程编号/班号" type="text" courseType="TYKC"/>

&#x20;                   </div>

&#x20;               </div>

&#x20;               

&#x20;           </header>



&#x20;           <!--体育课列表-->

&#x20;           <div class="cv-sport-course" cv-role="tabs">

&#x20;               <div id="cvCanSelectSportCourse" class="cv-tab-pane cv-active"></div>

&#x20;           </div>

&#x20;       </article>



&#x20;       <!-- 辅修课模块 -->

&#x20;       <article id="cvMinorCourse" class="cv-block-hide cv-pb-38">

&#x20;           <!--头部-->

&#x20;           <header class="cv-course-header cv-clearfix-child">

&#x20;               <div class="">

&#x20;                   <!--标题-->

&#x20;                   <!-- <h3 class="cv-mb-8" id="minorTitle">辅修选课</h3> -->

&#x20;                   <!--说明-->

&#x20;                   <span class="cv-caption-text" id="minorSpan"></span>

&#x20;                   <span class="credits">

&#x20;                   	<span class="credit-label" data-i18n-text="bxqzxzgxkxf">本学期主修最高选课学分</span>：

&#x20;                   	<span class="max-credit-value"></span>

&#x20;                   	<span class="credit-label" data-i18n-text="bxqzxyxxf">本学期主修已选学分</span>：

&#x20;                   	<span class="selected-credit-value"></span>

&#x20;                   	<span class="credit-label" data-i18n-text="bxqfxzgxkxf">本学期辅修最高选课学分</span>：

&#x20;                   	<span class="max-credit-value-fx"></span>

&#x20;                   	<span class="credit-label" data-i18n-text="bxqfxyxxf">本学期辅修已选学分</span>：

&#x20;                   	<span class="selected-credit-value-fx"></span>

&#x20;                   </span>

&#x20;                   <div style="padding-top:5px;padding-bottom:5px">

&#x20;                       <label data-i18n-text="isConflict">是否冲突</label>：

&#x20;                       <select class="cv-search-input search\_sfct" id="minor\_sfct" courseType="FXKC">

&#x20;                           <option value="2" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                           <option value="1" data-i18n-text="isConflict">冲突</option>

&#x20;                           <option value="0" data-i18n-text="noConflict">不冲突</option>

&#x20;                       </select>

&#x20;                       <label data-i18n-text="isFull" >是否已满</label>：

&#x20;                       <select class="cv-search-input search\_sfym" id="minor\_sfym" courseType="FXKC">

&#x20;                           <option value="2" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                           <option value="1"  data-i18n-text="full">已满</option>

&#x20;                           <option value="0"  data-i18n-text="empty">未满</option>

&#x20;                       </select>   

&#x20;                       <label data-i18n-text="query.kcxz">课程性质</label>：

&#x20;                       <select class="cv-search-input search\_kcxz" id="minor\_kcxz" courseType="FXKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select>

&#x20;                       <label class="search\_kclb\_label" data-i18n-text="kclb">课程类别</label>：

&#x20;                       <select class="cv-search-input search\_kclb" id="minor\_kclb" courseType="FXKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select>

&#x20;                       <input id="minorSearch" class="cv-search-input cv-search-input-key" data-i18n-placeholder="query.placeholder2" placeholder="请输入课程名称/上课教师/课程编号/班号" type="text" courseType="FXKC"/>

&#x20;                   </div>

&#x20;                   <div class="cv-minor-njyxzy" style="padding-top:5px;padding-bottom:5px;">

&#x20;                       <label data-i18n-text="query.nj">年级</label>：

&#x20;                       <select class="cv-search-input search\_nj" id="minor\_nj" courseType="FXKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select>

&#x20;                       <label data-i18n-text="query.yx">院系</label>：

&#x20;                       <select class="cv-search-input search\_yx" id="minor\_yx" courseType="FXKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select>

&#x20;                       <label data-i18n-text="query.zy">专业</label>：

&#x20;                       <select class="cv-search-input search\_zy" id="minor\_zy" courseType="FXKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select>

&#x20;                   </div>

&#x20;               </div>                

&#x20;           </header>



&#x20;           <!--辅修课列表-->

&#x20;           <div class="cv-minor-course" cv-role="tabs">

&#x20;               <div id="cvCanSelectMinorCourse" class="cv-tab-pane cv-active"></div>

&#x20;           </div>

&#x20;       </article>



&#x20;       <!--全校课程模块-->

&#x20;       <article id="cvSchoolCourse" class="cv-block-hide cv-pb-38">

&#x20;           <!--头部-->

&#x20;           <header class="cv-course-header cv-clearfix-child">

&#x20;               <div class="">

&#x20;                   <!--标题-->

&#x20;                   <!-- <h3 class="cv-mb-8" id="schoolTitle">全校课程</h3> -->

&#x20;                   <!--说明-->

&#x20;                   <span class="cv-caption-text" id="schoolSpan"></span>

&#x20;                   <span class="credits">

&#x20;                   	<span class="credit-label" data-i18n-text="bxqzgxkxf">本学期最高选课学分</span>：

&#x20;                   	<span class="max-credit-value"></span>

&#x20;                   	<span class="credit-label" data-i18n-text="bxqzgxkxf">本学期已选学分</span>：

&#x20;                   	<span class="selected-credit-value"></span>

&#x20;                   </span>

&#x20;                   <div style="padding-top:5px;padding-bottom:5px">

&#x20;                   	<label class="cv-search-label" data-i18n-text="pkdw">排课单位</label>：

&#x20;                       <select class="cv-search-input search\_kkdw" id="school\_kkdw" courseType="QXKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select> 

&#x20;                       <label class="cv-search-label search\_xgxklb\_label" style="width:100px" data-i18n-text="xgxklb">通识课类别 </label>：

&#x20;                       <select class="cv-search-input search\_xgxklb" id="school\_xgxklb" courseType="QXKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select>

&#x20;                       <label class="cv-search-label" data-i18n-text="sksj">上课时间</label>：

&#x20;                       <select class="cv-search-input search\_skxq" id="school\_skxq" courseType="QXKC"></select>

&#x20;                       <select class="cv-search-input search\_ksjc" id="school\_ksjc" courseType="QXKC"></select>

&#x20;                       <select class="cv-search-input search\_jsjc" id="school\_jsjc" courseType="QXKC"></select>

&#x20;                       <input id="schoolSearch" class="cv-search-input cv-search-input-key" data-i18n-placeholder="query.placeholder2" placeholder="请输入课程名称/上课教师/课程编号/班号" type="text" courseType="QXKC"/>

&#x20;                   </div>

&#x20;               </div>

&#x20;           </header>



&#x20;           <!--全校课程列表-->

&#x20;           <div class="cv-school-course" cv-role="tabs">

&#x20;               <div id="cvCanSelectSchoolCourse" class="cv-tab-pane cv-active"></div>

&#x20;           </div>

&#x20;       </article>



&#x20;       <!--分离的全校课程模块-暨南大学定制-->

&#x20;       <article id="cvSplitSchoolCourse" class="cv-block-hide cv-pb-38">

&#x20;           <!--头部-->

&#x20;           <header class="cv-course-header cv-clearfix-child">

&#x20;               <div class="">

&#x20;                   <!--标题-->

&#x20;                   <!-- <h3 class="cv-mb-8" id="schoolTitle">全校课程</h3> -->

&#x20;                   <!--说明-->

&#x20;                   <span class="cv-caption-text" id="splitSchoolSpan"></span>

&#x20;                   <span class="credits">

&#x20;                   	<span class="credit-label" data-i18n-text="bxqzxzgxkxf">本学期主修最高选课学分</span>：

&#x20;                   	<span class="max-credit-value"></span>

&#x20;                   	<span class="credit-label" data-i18n-text="bxqzxyxxf">本学期主修已选学分</span>：

&#x20;                   	<span class="selected-credit-value"></span>

&#x20;                   	<span class="credit-label" data-i18n-text="bxqfxzgxkxf">本学期辅修最高选课学分</span>：

&#x20;                   	<span class="max-credit-value-fx"></span>

&#x20;                   	<span class="credit-label" data-i18n-text="bxqfxyxxf">本学期辅修已选学分</span>：

&#x20;                   	<span class="selected-credit-value-fx"></span>

&#x20;                   </span>

&#x20;                   <div style="padding-top: 5px;">

&#x20;                       <input id="splitSchoolSearch" style="margin: 0;" class="cv-search-input cv-search-input-key" data-i18n-placeholder="query.placeholder2" placeholder="请输入课程名称/上课教师/课程编号/班号/课组名称" type="text" courseType="FLQXKC"/>

&#x20;                   	<button class="bh-btn bh-btn-default" id="splitSearchBtn" data-i18n-text="search">搜索</button>

&#x20;                   </div>

&#x20;                   <div style="padding-top:5px;padding-bottom:5px">

&#x20;                   	<label class="cv-search-label" data-i18n-text="pkdw">排课单位</label>：

&#x20;                       <select class="cv-search-input search\_kkdw" id="splitSchool\_kkdw" courseType="FLQXKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select> 

&#x20;                       <label class="cv-search-label search\_xgxklb\_label" style="width:100px" data-i18n-text="xgxklb">通识课类别 : </label>：

&#x20;                       <select class="cv-search-input search\_xgxklb" id="splitSchool\_xgxklb" courseType="FLQXKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select>

&#x20;                       <label class="cv-search-label" data-i18n-text="credit">学分</label>：

&#x20;                       <select class="cv-search-input search\_kcxf" id="splitSchool\_kcxf" courseType="FLQXKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select>

&#x20;                       <label class="cv-search-label" data-i18n-text="campus">校区</label>：

&#x20;                       <select class="cv-search-input search\_xq" id="splitSchool\_xq" courseType="FLQXKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select>

&#x20;                       <label class="cv-search-label" data-i18n-text="sfmk">是否慕课</label>：

&#x20;                       <select class="cv-search-input search\_sfmooc" id="splitSchool\_sfmooc" courseType="FLQXKC">

&#x20;                           <option value="" selected="selected" data-i18n-text="pleaseChoose">--请选择--</option>

&#x20;                       </select>

&#x20;                       <label class="cv-search-label" data-i18n-text="sksj">上课时间</label>：

&#x20;                       <select class="cv-search-input search\_skxq" id="splitSchool\_skxq" courseType="FLQXKC"></select>

&#x20;                       <select class="cv-search-input search\_ksjc" id="splitSchool\_ksjc" courseType="FLQXKC"></select>

&#x20;                       <select class="cv-search-input search\_jsjc" id="splitSchool\_jsjc" courseType="FLQXKC"></select>

&#x20;                   </div>

&#x20;               </div>

&#x20;           </header>



&#x20;           <!--全校课程列表-->

&#x20;           <div class="cv-splitSchool-course" cv-role="tabs">

&#x20;               <div id="cvCanSelectSplitSchoolCourse" class="cv-tab-pane cv-active"></div>

&#x20;           </div>

&#x20;       </article>



&#x20;       <!--侧边栏-->

&#x20;       <aside id="cvAside" class="cv-aside">

&#x20;           <!--mini条-->

&#x20;           <div class="cv-mini">

&#x20;               <div class="cv-icons">

&#x20;                   <!--用户信息-->

&#x20;                   <div class="cv-user-icon cvMiniIconFlag" type="user" data-i18n-title="home.myInformation" title="我的信息">

&#x20;                       <img src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/images/curriculaVariable/user-icon.png?av=1781150761398">

&#x20;                   </div>

&#x20;                   <!--课表-->

&#x20;                   <div class="cv-course-icon cvMiniIconFlag" type="course" data-i18n-title="home.myClassSchedule" title="我的课表">

&#x20;                       <img src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/images/curriculaVariable/course-icon.png?av=1781150761398">

&#x20;                   </div>

&#x20;                   <!--落选课程-->

&#x20;                   <div class="cv-unsuccessful-icon cvMiniIconFlag" type="unsuccessful" data-i18n-title="home.lostCourse" title="落选课程">

&#x20;                       <img src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/images/curriculaVariable/unsuccessful-icon.png?av=1781150761398">

&#x20;                   </div> 

&#x20;                   <!--切换轮次-->

&#x20;                   <div class="cv-batch-icon cvMiniIconFlag" type="batch" data-i18n-title="changeElectiveBatch" title="切换轮次">

&#x20;                       <img src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/images/curriculaVariable/change-electiveBatch.png?av=1781150761398">

&#x20;                   </div>

&#x20;                   <!--查看成绩-->

&#x20;                   <div class="cv-batch-icon cvMiniIconFlag" type="score" data-i18n-title="home.viewGrades" title="查看成绩">

&#x20;                       <img src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/images/curriculaVariable/score.png?av=1781150761398">

&#x20;                   </div>

&#x20;                   <!--已选志愿/退课日志-->

&#x20;                   <div class="cv-choice-icon cv-active cvMiniIconFlag" type="grablessons">

&#x20;                       <img src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/images/curriculaVariable/choice-icon.png?av=1781150761398">

&#x20;                       <div class="cv-num" id="selectcourse\_num"></div>                

&#x20;                       <div class="cv-text" data-i18n-text="home.selectedCourse" type="grablessons">已选课程</div>                        

&#x20;                   </div>

&#x20;               </div>



&#x20;               <!--回到顶部按钮-->

&#x20;               <div class="cv-top cvMiniIconFlag" type="top">TOP</div>

&#x20;           </div>



&#x20;           <!-- 侧边栏内容 -->

&#x20;           <div class="cv-content">

&#x20;               <!-- 学生信息 -->

&#x20;               <div id="cvAsideUser" class="cv-user"></div>

&#x20;               <!--课表模块-->

&#x20;               <div id="cvAsideCourse" class="cv-aside-course"></div>

&#x20;               <!--落选课程-->

&#x20;               <div id="cvUnsuccessfulCourse" class="cv-aside-selected-course" style="height:100%"></div>

&#x20;               <!--已选课程模块-->

&#x20;               <div id="cvAsideChoice" class="cv-aside-choice cv-active"></div>

&#x20;               <!-- 切换轮次 -->

&#x20;               <div id="cvAsideChangeBatch" class="cv-aside-change-batch"></div>

&#x20;           </div>

&#x20;       </aside>



&#x20;       

&#x20;       <!--页脚-->

&#x20;       <footer class="cv-page-footer">

&#x20;           <div class="cv-copyright" id="cv-copyright" data-i18n-text="index.copyrightInformation">

&#x20;           	<div id="noline-tip"></div>	

<!--             	<div>版权信息：© 2016 江苏金智教育信息股份有限公司 苏ICP备10204514号</div>

&#x20;-->            </div>

&#x20;       </footer>



&#x20;       <div class="cv-dialog" style="display: none">

&#x20;           <div>

&#x20;               <div class="cv-body">

&#x20;                   <img class="cv-mb-16" src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/images/curriculaVariable/dialog-icon.png?av=1781150761398">

&#x20;                   <h2 class="cv-mb-8">确认退选</h2>

&#x20;                   <div class="cv-mb-8">《<span>数字媒体装置艺术构成</span>》</div>

&#x20;                   <div>这门课程吗？</div>

&#x20;               </div>

&#x20;               <div class="cv-foot">

&#x20;                   <div class="cv-sure">退选</div>

&#x20;                   <div class="cv-cancel">取消</div>

&#x20;               </div>

&#x20;           </div>

&#x20;       </div>

&#x20;   </div>



&#x20;   <!-- 引导页 -->

&#x20;   <div class='jszp' style="display:none;">

&#x20;       <div class='step1'>

&#x20;           <div>

&#x20;             <img src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/images/curriculaVariable/01.png?av=1781150761398">  

&#x20;           </div>

&#x20;           <div class="btns">

&#x20;               <div class='cv-btn'>我知道了</div>

&#x20;           </div>

&#x20;       </div>

&#x20;       <div class='step2' style="display: none;">

&#x20;           <div>

&#x20;             <img src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/images/curriculaVariable/02.png?av=1781150761398">  

&#x20;           </div>

&#x20;           <div class="btns">

&#x20;               <div class='cv-btn'>我知道了</div>

&#x20;           </div>

&#x20;       </div>

&#x20;   </div>



&#x09;<!--推荐选课的专家模式列表外框的模板-->

&#x09;<script type="text/template" id="tpl-recommend-list">

&#x09;    <div class="cv-list recommend-list">

&#x09;        <div class="cv-head">

&#x20;               <div class="cv-normal cv-num">@kch</div>

&#x20;               <div class="cv-normal cv-course">@kcm</div>

&#x20;               <div class="cv-sort cv-class" id="recommendSort">@kxbjs</div>

&#x20;               <div class="cv-normal cv-type">@kclb</div>

&#x20;               <div class="cv-normal cv-nature">@kcxz</div>

&#x20;               <div class="cv-normal cv-department-col">@kkdw</div>

&#x20;               <div class="cv-normal cv-credit-col">@credit</div>

&#x09;        </div>

&#x09;        <div class="cv-body" id="recommendBody">

&#x09;            @body

&#x09;        </div>

&#x20;           <div class="cv-foot" style="padding-top:20px">

&#x20;               <a class="" href="javascript:void(0);" id="recommendUp">@pageup</a>

&#x20;              	<span style="padding: 0 10px;">@pagetotal1 <span id="recommendTotalPage">@totalPage</span> @pagetotal2 <span id="recommendPageNumber">@pageNumber</span> @pagetotal3</span>

&#x20;               <a class="" href="javascript:void(0);" id="recommendDown">@pagedown</a>

&#x20;           </div>

&#x09;    </div>

&#x09;</script>

&#x09;<!--推荐选课的专家模式列表每行的内容模板-->

&#x09;<script type="text/template" id="tpl-recommend-list-row">

&#x09;    <div class="cv-row @selectedClass" coursenumber="@courseNumber" index="@index" isChoose="@isChoose">

&#x09;        <div class="cv-num">

&#x09;			<span class="cv-courseFlag @courseFlagDisplay">@courseFlag</span>

&#x09;			<span class="num-value">@number</span>

&#x09;			<div style="display: @hascourseDetail;">

&#x09;				<a class="cv-detail" data-num="@jxbNumber" href="javascript:void(0);">@kcdetail</a>

&#x09;			</div>

&#x09;		</div>

&#x20;           <div class="cv-course">@title</div>

&#x20;           <div class="cv-class">@class</div>

&#x20;           <div class="cv-type">@type</div>

&#x20;           <div class="cv-nature">@nature</div>

&#x20;           <div class="cv-department-col">@department</div>

&#x20;           <div class="cv-credit-col">@credit</div>

&#x09;    </div>

&#x09;</script>



&#x20;   <!--辅修选课的列表外框的模板-->

&#x20;   <script type="text/template" id="tpl-minor-list">

&#x20;       <div class="cv-list minor-list">

&#x20;           <div class="cv-head">

&#x20;               <div class="cv-normal cv-num">@kch</div>

&#x20;               <div class="cv-normal cv-course">@kcm</div>

&#x20;               <div class="cv-sort cv-class" id="minorSort">@kxbjs</div>

&#x20;               <div class="cv-normal cv-type">@kclb</div>

&#x20;               <div class="cv-normal cv-nature">@kcxz</div>

&#x20;               <div class="cv-normal cv-department-col">@kkdw</div>

&#x20;               <div class="cv-normal cv-credit-col">@credit</div>

&#x20;           </div>

&#x20;           <div class="cv-body" id="minorBody">

&#x20;               @body

&#x20;           </div>

&#x20;           <div class="cv-foot" style="padding-top:20px">

&#x20;               <a class="" href="javascript:void(0);" id="minorUp">@pageup</a>

&#x20;               <span style="padding: 0 10px;">@pagetotal1 <span id="minorTotalPage">@totalPage</span> @pagetotal2 <span id="minorPageNumber">@pageNumber</span> @pagetotal3</span>

&#x20;               <a class="" href="javascript:void(0);" id="minorDown">@pagedown</a>

&#x20;           </div>

&#x20;       </div>

&#x20;   </script>

&#x20;   <!--辅修选课的列表每行的内容模板-->

&#x20;   <script type="text/template" id="tpl-minor-list-row">

&#x20;       <div class="cv-row @selectedClass" coursenumber="@courseNumber" index="@index" isChoose="@isChoose">

&#x09;		<div class="cv-num">

&#x09;			<span class="cv-courseFlag @courseFlagDisplay">@courseFlag</span>

&#x09;			<span class="num-value">@number</span>

&#x09;			<div style="display: @hascourseDetail;">

&#x09;				<a class="cv-detail" data-num="@jxbNumber" href="javascript:void(0);">@kcdetail</a>

&#x09;			</div>

&#x09;		</div>

&#x20;           <div class="cv-course">@title</div>

&#x20;           <div class="cv-class">@class</div>

&#x20;           <div class="cv-type">@type</div>

&#x20;           <div class="cv-nature">@nature</div>

&#x20;           <div class="cv-department-col">@department</div>

&#x20;           <div class="cv-credit-col">@credit</div>

&#x20;       </div>

&#x20;   </script>



&#x20;   <!--方案内选课列表外框的模板 -->

&#x20;   <script type="text/template" id="tpl-program-list">

&#x20;       <div class="cv-list program-list">

&#x20;           <div class="cv-head">

&#x20;               <div class="cv-normal cv-num">@kch</div>

&#x20;               <div class="cv-normal cv-course">@kcm</div>

&#x20;               <div class="cv-sort cv-class" id="programSort">@kxbjs</div>

&#x20;               <div class="cv-normal cv-type">@kclb</div>

&#x20;               <div class="cv-normal cv-nature">@kcxz</div>

&#x20;               <div class="cv-normal cv-department-col">@kkdw</div>

&#x20;               <div class="cv-normal cv-credit-col">@credit</div>

&#x20;           </div>

&#x20;           <div class="cv-body" id="programBody">

&#x20;               @body

&#x20;           </div>

&#x20;           <div class="cv-foot" style="padding-top:20px">

&#x20;               <a class="" href="javascript:void(0);" id="programUp">@pageup</a>

&#x20;               <span style="padding: 0 10px;">@pagetotal1 <span id="programTotalPage">@totalPage</span> @pagetotal2 <span id="programPageNumber">@pageNumber</span> @pagetotal3</span>

&#x20;               <a class="" href="javascript:void(0);" id="programDown">@pagedown</a>

&#x20;           </div>

&#x20;       </div>

&#x20;   </script>

&#x20;   <!--方案内选课列表每行的内容模板-->

&#x20;   <script type="text/template" id="tpl-program-list-row">

&#x20;       <div class="cv-row @selectedClass" coursenumber="@courseNumber" index="@index" isChoose="@isChoose">

&#x20;           <div class="cv-num">

&#x09;			<span class="cv-courseFlag @courseFlagDisplay">@courseFlag</span>

&#x09;			<span class="num-value">@number</span>

&#x09;			<div style="display: @hascourseDetail;">

&#x09;				<a class="cv-detail" data-num="@jxbNumber" href="javascript:void(0);">@kcdetail</a>

&#x09;			</div>

&#x09;		</div>

&#x20;           <div class="cv-course">@title</div>

&#x20;           <div class="cv-class">@class</div>

&#x20;           <div class="cv-type">@type</div>

&#x20;           <div class="cv-nature">@nature</div>

&#x20;           <div class="cv-department-col">@department</div>

&#x20;           <div class="cv-credit-col">@credit</div>

&#x20;       </div>

&#x20;   </script>



&#x20;   <!--方案外选课列表外框的模板 -->

&#x20;   <script type="text/template" id="tpl-unprogram-list">

&#x20;       <div class="cv-list unprogram-list">

&#x20;           <div class="cv-head">

&#x20;               <div class="cv-normal cv-num">@kch</div>

&#x20;               <div class="cv-normal cv-course">@kcm</div>

&#x20;               <div class="cv-sort cv-class" id="unProgramSort">@kxbjs</div>

&#x20;               <div class="cv-normal cv-type">@kclb</div>

&#x20;               <div class="cv-normal cv-nature">@kcxz</div>

&#x20;               <div class="cv-normal cv-Major">@zfx</div>

&#x20;               <div class="cv-normal cv-department-col">@kkdw</div>

&#x20;               <div class="cv-normal cv-credit-col">@credit</div>

&#x20;           </div>

&#x20;           <div class="cv-body" id="unProgramBody">

&#x20;               @body

&#x20;           </div>

&#x20;           <div class="cv-foot" style="padding-top:20px">

&#x20;               <a class="" href="javascript:void(0);" id="unProgramUp">@pageup</a>

&#x20;               <span style="padding: 0 10px;">@pagetotal1 <span id="unProgramTotalPage">@totalPage</span> @pagetotal2 <span id="unProgramPageNumber">@pageNumber</span> @pagetotal3</span>

&#x20;               <a class="" href="javascript:void(0);" id="unProgramDown">@pagedown</a>

&#x20;           </div>

&#x20;       </div>

&#x20;   </script>

&#x20;   <!--方案外选课列表每行的内容模板-->

&#x20;   <script type="text/template" id="tpl-unprogram-list-row">

&#x20;       <div class="cv-row @selectedClass" coursenumber="@courseNumber" index="@index" isChoose="@isChoose">

&#x20;           <div class="cv-num">

&#x09;			<span class="cv-courseFlag @courseFlagDisplay">@courseFlag</span>

&#x09;			<span class="num-value">@number</span>

&#x09;			<div style="display: @hascourseDetail;">

&#x09;				<a class="cv-detail" data-num="@jxbNumber" href="javascript:void(0);">@kcdetail</a>

&#x09;			</div>

&#x09;		</div>

&#x20;           <div class="cv-course">@title <span class="cv-faDetail" data-num="@jxb1Number">@ssfa</span></div>

&#x20;           <div class="cv-class">@class</div>

&#x20;           <div class="cv-type">@type</div>

&#x20;           <div class="cv-nature">@nature</div>

&#x09;		<div class="cv-Major">@majorFlag</div>

&#x20;           <div class="cv-department-col">@department</div>

&#x20;           <div class="cv-credit-col">@credit</div>

&#x20;       </div>

&#x20;   </script>



&#x20;   <!--所属方案内容模板-->

&#x20;   <script type="text/template" id="tpl-syfa-list">

&#x20;       <table class="syfa-table">

&#x20;           <thead>			

&#x20;               <tr>

&#x09;			    <th class="nj">@grade </th>

&#x09;			    <th class="kclb">@kclb </th>

&#x09;			    <th class="kcxz">@kcxz </th>

&#x09;			    <th class="famc">@ssfa </th>

&#x09;		    </tr>

&#x20;           </thead>

&#x20;           <tbody>

&#x09;		    @syfabody

&#x20;           </tbody>

&#x09;	</table>

&#x09;	<div class="cv-syfa-foot">

&#x20;           <a class="" href="javascript:void(0);" id="unProgramFalistUp">@pageup</a>

&#x20;           <span style="padding: 0 10px;">@pagetotal1 <span id="unProgramFalistTotalPage"></span> @pagetotal2 <span id="unProgramFalistPageNumber"></span> @pagetotal3</span>

&#x20;           <a class="" href="javascript:void(0);" id="unProgramFalistDown">@pagedown</a>

&#x20;       </div>

&#x20;   </script>



&#x20;   <!--重修选课列表外框的模板 -->

&#x20;   <script type="text/template" id="tpl-retake-list">

&#x20;       <div class="cv-list retake-list">

&#x20;           <div class="cv-head">

&#x20;               <div class="cv-normal cv-num">@kch</div>

&#x20;               <div class="cv-normal cv-course">@kcm</div>

&#x20;               <div class="cv-sort cv-class" id="retakeSort">@kxbjs</div>

&#x20;               <div class="cv-normal cv-type">@kclb</div>

&#x20;               <div class="cv-normal cv-nature">@kcxz</div>

&#x20;               <div class="cv-normal cv-department-col">@kkdw</div>

&#x20;               <div class="cv-normal cv-credit-col">@credit</div>

&#x09;			<div class="cv-normal cv-cxxklx">@xklx</div>

&#x20;           </div>

&#x20;           <div class="cv-body" id="retakeBody">

&#x20;               @body

&#x20;           </div>

&#x20;           <div class="cv-foot" style="padding-top:20px">

&#x20;               <a class="" href="javascript:void(0);" id="retakeUp">@pageup</a>

&#x20;               <span style="padding: 0 10px;">@pagetotal1 <span id="retakeTotalPage">@totalPage</span> @pagetotal2 <span id="retakePageNumber">@pageNumber</span> @pagetotal3</span>

&#x20;               <a class="" href="javascript:void(0);" id="retakeDown">@pagedown</a>

&#x20;           </div>

&#x20;       </div>

&#x20;   </script>

&#x20;   <!--重修选课列表每行的内容模板-->

&#x20;   <script type="text/template" id="tpl-retake-list-row">

&#x20;       <div class="cv-row @selectedClass" coursenumber="@courseNumber" index="@index" isChoose="@isChoose">

&#x20;           <div class="cv-num">

&#x09;			<span class="cv-courseFlag @courseFlagDisplay">@courseFlag</span>

&#x09;			<span class="num-value">@number</span>

&#x09;			<div style="display: @hascourseDetail;">

&#x09;				<a class="cv-detail" data-num="@jxbNumber" href="javascript:void(0);">@kcdetail</a>

&#x09;			</div>

&#x09;		</div>

&#x20;           <div class="cv-course">@title</div>

&#x20;           <div class="cv-class">@class</div>

&#x20;           <div class="cv-type">@type</div>

&#x20;           <div class="cv-nature">@nature</div>

&#x20;           <div class="cv-department-col">@department</div>

&#x20;           <div class="cv-credit-col">@credit</div>

&#x20;           <div class="cv-cxxklx">@cxxklx</div>

&#x20;       </div>

&#x20;   </script>



&#x20;   <!--体育选课列表外框的模板 -->

&#x20;   <script type="text/template" id="tpl-sport-list">

&#x20;       <div class="cv-list sport-list">

&#x20;           <div class="cv-head">

&#x20;               <div class="cv-normal cv-num">@kch</div>

&#x20;               <div class="cv-normal cv-course">@kcm</div>

&#x20;               <div class="cv-sort cv-class" id="sportSort">@kxbjs</div>

&#x20;               <div class="cv-normal cv-type">@kclb</div>

&#x20;               <div class="cv-normal cv-nature">@kcxz</div>

&#x20;               <div class="cv-normal cv-department-col">@kkdw</div>

&#x20;               <div class="cv-normal cv-credit-col">@credit</div>

&#x20;           </div>

&#x20;           <div class="cv-body" id="sportBody">

&#x20;               @body

&#x20;           </div>

&#x20;           <div class="cv-foot" style="padding-top:20px">

&#x20;               <a class="" href="javascript:void(0);" id="sportUp">@pageup</a>

&#x20;               <span style="padding: 0 10px;">@pagetotal1 <span id="sportTotalPage">@totalPage</span> @pagetotal2 <span id="sportPageNumber">@pageNumber</span> @pagetotal3<span>

&#x20;               <a class="" href="javascript:void(0);" id="sportDown">@pagedown</a>

&#x20;           </div>

&#x20;       </div>

&#x20;   </script>

&#x20;   <!--体育选课列表每行的内容模板-->

&#x20;   <script type="text/template" id="tpl-sport-list-row">

&#x20;       <div class="cv-row @selectedClass" coursenumber="@courseNumber" index="@index" isChoose="@isChoose">

&#x20;           <div class="cv-num">

&#x09;			<span class="cv-courseFlag @courseFlagDisplay">@courseFlag</span>

&#x09;			<span class="num-value">@number</span>

&#x09;			<div style="display: @hascourseDetail;">

&#x09;				<a class="cv-detail" data-num="@jxbNumber" href="javascript:void(0);">@kcdetail</a>

&#x09;			</div>

&#x09;		</div>

&#x20;           <div class="cv-course">@title</div>

&#x20;           <div class="cv-class">@class</div>

&#x20;           <div class="cv-type">@type</div>

&#x20;           <div class="cv-nature">@nature</div>

&#x20;           <div class="cv-department-col">@department</div>

&#x20;           <div class="cv-credit-col">@credit</div>

&#x20;       </div>

&#x20;   </script>



&#x09;<!--公选课的列表外框的模板-->

&#x09;<script type="text/template" id="tpl-public-list">

&#x09;    <div class="cv-list public-list">

&#x09;        <div class="cv-head">

&#x09;            <div class="cv-normal cv-setting-col">@cz</div>

&#x09;            <div class="cv-normal cv-public-number-col">@kch</div>

&#x20;               <div class="cv-normal cv-public-title-col">@kcm</div>

&#x09;			<div class="cv-normal cv-public-jxbid-col">@bh</div>

&#x09;			<div class="cv-normal cv-public-time-col">@timeplace</div>

&#x09;			<div class="cv-normal cv-public-examTime-col">@kssj</div>

&#x20;               <div class="cv-normal cv-public-campus-col">@campus</div>

&#x20;               <div class="cv-normal cv-public-department-col">@kkdw</div>

&#x20;               <div class="cv-normal cv-public-nature-col">@kcxz</div>

&#x20;               <div class="cv-normal cv-public-type-col">@kclb</div>

&#x09;			<div class="cv-normal cv-public-type-col">@xgxklb</div>

&#x09;			<div class="cv-normal cv-public-skyz-col">@skyy</div>

&#x09;			<div class="cv-normal cv-public-capcity-col">@yxkrl</div>

&#x20;               <div class="cv-normal cv-public-credit-col">@credit</div>

&#x20;               <div class="cv-normal cv-public-examTypeName-col">@kslx</div>

&#x20;               <div class="cv-normal cv-public-teacher-col">@skjs</div>

&#x09;        </div>

&#x09;        <div class="cv-body" id="publicBody">

&#x09;            @body

&#x09;        </div>

&#x20;           <div class="cv-foot" style="padding-top:20px">

&#x20;               <a class="" href="javascript:void(0);" id="publicUp">@pageup</a>

&#x20;               <span style="padding: 0 10px;">@pagetotal1 <span id="publicTotalPage">@totalPage</span> @pagetotal2 <span id="publicPageNumber">@pageNumber</span> @pagetotal3</span>

&#x20;               <a class="" href="javascript:void(0);" id="publicDown">@pagedown</a>

&#x20;           </div>

&#x09;    </div>

&#x09;</script>

&#x09;<!--公选课的列表每行的内容模板-->

&#x09;<script type="text/template" id="tpl-public-list-row">

&#x09;    <div class="cv-row">

&#x09;        <div class="cv-setting-col @selectedClass">

&#x09;            <button class="cv-btn cv-tag">@volunteerText</button>

&#x09;            <a class="cv-choice @display @cv-disabled" extInfo="@extInfo" retakeTypeDetail="@retakeTypeDetail" retakeType="@retakeType" campus="@campus" teachCampus="@teachCampus" number="@number" tcId="@tcId" capacitySuffix="@capacitySuffix" isFull="@isFull" isConflict="@isConflict" limitGender="@limitGender" capacityOfMale="@capacityOfMale" capacityOfFemale="@capacityOfFemale" numberOfMale="@numberOfMale" numberOfFemale="@numberOfFemale" hasTest="@hasTest" isHasCj="@isHasCj" href="javascript:void(0);" @isDisabled>@choose</a>

&#x09;        </div>

&#x09;        <div class="cv-public-number-col">@allCourseNumber</div>

&#x20;           <div class="cv-public-title-col">

&#x09;			@courseName

&#x09;			<span class="cv-courseFlag @courseFlagDisplay">@courseFlag</span>

&#x09;		</div>

&#x09;		<div class="cv-public-jxbid-col">@teachingClassID</div>

&#x09;		<div class="cv-public-time-col" title="@timeTitle">@time</div>

&#x09;		<div class="cv-normal cv-public-examTime-col">@examTime</div>

&#x09;		<div class="cv-public-campus-col">@campusName</div>

&#x20;           <div class="cv-public-department-col">@departmentName</div>

&#x20;           <div class="cv-public-nature-col">@courseNatureName</div>

&#x20;           <div class="cv-public-type-col">@courseTypeName</div>

&#x09;		<div class="cv-public-xgxklb-col">@type<br/>@courseSection</div>

&#x09;		<div class="cv-public-skyz-col">@teachLanguage</div>

&#x09;		<div class="cv-public-capcity-col">@capcity</div>

&#x20;           <div class="cv-public-credit-col">@credit</div>

&#x20;           <div class="cv-public-examTypeName-col">@examTypeName</div>

&#x20;           <div class="cv-public-teacher-col">@teacherName</div>

&#x09;    </div>

&#x09;</script>



&#x20;   <!--全校课程的列表外框的模板-->

&#x20;   <script type="text/template" id="tpl-school-list">

&#x20;       <div class="cv-list school-list @showAllKcClass">

&#x20;           <div class="cv-head cv-school" style="height:48px;padding:5px 0">

&#x09;			<div class="cv-normal cv-school-cz-col">@cz</div>

&#x20;               <div class="cv-normal cv-school-number-col">@kch</div>

&#x20;               <div class="cv-normal cv-school-title-col">@kcm</div>

&#x20;               <div class="cv-normal cv-school-index-col">@bh</div>

&#x20;               <div class="cv-normal cv-school-time-col">@timeplace</div>

&#x20;               <div class="cv-normal cv-school-campus-col">@campus</div>

&#x20;               <div class="cv-normal cv-school-department-col">@kkdw</div>

&#x20;               <div class="cv-normal cv-school-nature-col">@kcxz</div>

&#x20;               <div class="cv-normal cv-school-type-col">@kclb</div>

&#x09;			<div class="cv-normal cv-school-capcity-col">@yxkrl</div>

&#x20;               <div class="cv-normal cv-school-credit-col">@credit</div>

&#x20;               <div class="cv-normal cv-school-examTypeName-col">@kslx</div>

&#x20;               <div class="cv-normal cv-school-teacher-col">@teacher</div>

&#x20;           </div>

&#x20;           <div class="cv-body" id="schoolBody">

&#x20;               @body

&#x20;           </div>

&#x20;           <div class="cv-foot" style="padding-top:20px">

&#x20;               <a class="" href="javascript:void(0);" id="schoolUp">@pageup</a>

&#x20;               <span style="padding: 0 10px;">@pagetotal1 <span id="schoolTotalPage">@totalPage</span> @pagetotal2 <span id="schoolPageNumber">@pageNumber</span> @pagetotal3</span>

&#x20;               <a class="" href="javascript:void(0);" id="schoolDown">@pagedown</a>

&#x20;           </div>

&#x20;       </div>

&#x20;   </script>

&#x20;   <!--全校课程的列表每行的内容模板-->

&#x20;   <script type="text/template" id="tpl-school-list-row">

&#x20;       <div class="cv-row row-school-link">

&#x09;		<div class="cv-school-cz-col cv-setting-col @selectedClass">

&#x09;			<a href="javascript:void(0)" class="row-school-index" index="@index">检查</a>

&#x09;			<button class="cv-btn cv-tag">@volunteerText</button>

&#x09;			<a class="cv-choice @display @disable" isConflict="@isConflict" retakeTypeDetail="@retakeTypeDetail" retakeType="@retakeType" limitGender="@limitGender" campus="@campus" teachCampus="@teachCampus" number="@number" tcId="@tcId" hasTest="@hasTest" isHasCj="@isHasCj" href="javascript:void(0);" @isDisabled>@xz</a>

&#x09;		</div>

&#x20;           <div class="cv-school-number-col">@allCourseNumber</div>

&#x20;           <div class="cv-school-title-col">

&#x09;			@courseName

&#x09;			<span class="cv-courseFlag @courseFlagDisplay">@courseFlag</span>

&#x09;		</div>

&#x20;           <div class="cv-school-index-col">@teachingClassID</div>

&#x09;		<div class="cv-school-time-col" title="@timeTitle">@time</div>

&#x09;		<div class="cv-school-campus-col">@campusName</div>

&#x20;           <div class="cv-school-department-col">@departmentName</div>

&#x20;           <div class="cv-school-nature-col">@courseNatureName</div>

&#x20;           <div class="cv-school-type-col">@courseTypeName</div>

&#x09;		<div class="cv-school-capcity-col">@capcity</div>

&#x20;           <div class="cv-school-credit-col">@credit</div>

&#x20;           <div class="cv-school-examTypeName-col">@examTypeName</div>

&#x20;           <div class="cv-school-teacher-col">@teacherName</div>

&#x20;       </div>

&#x20;   </script>



&#x20;   <!--分离的全校课程的列表外框的模板-->

&#x20;   <script type="text/template" id="tpl-splitSchool-list">

&#x20;       <div class="cv-list splitSchool-list @showAllKcClass">

&#x20;           <div class="cv-head cv-school" style="height:48px;padding:5px 0">

&#x09;			<div class="cv-normal cv-school-cz-col">@cz</div>

&#x20;               <div class="cv-normal cv-school-number-col">@kch</div>

&#x20;               <div class="cv-normal cv-school-title-col">@kcm</div>

&#x09;			<div class="cv-normal cv-school-jxbid-col">@bh</div>

&#x09;			<div class="cv-normal cv-school-time-col">@timeplace</div>

&#x09;			<div class="cv-normal cv-school-examTime-col">@kssj</div>

&#x20;               <div class="cv-normal cv-school-campus-col">@campus</div>

&#x20;               <div class="cv-normal cv-school-department-col">@kkdw</div>

&#x20;               <div class="cv-normal cv-school-department-col">@kzmc</div>

&#x20;               <div class="cv-normal cv-school-nature-col">@kcxz</div>

&#x20;               <div class="cv-normal cv-school-type-col">@kclb</div>

&#x09;			<div class="cv-normal cv-school-rwxdlx-col">@sfzx</div>

&#x09;			<div class="cv-normal cv-school-type-col">@xgxklb</div>

&#x09;			<div class="cv-normal cv-school-sfmooc-col">@sfmk</div>

&#x09;			<div class="cv-normal cv-school-skyz-col">@skyy</div>

&#x09;			<div class="cv-normal cv-school-capcity-col">@yxkrl</div>

&#x20;               <div class="cv-normal cv-school-credit-col">@credit</div>

&#x20;               <div class="cv-normal cv-school-examTypeName-col">@kslx</div>

&#x20;               <div class="cv-normal cv-school-teacher-col">@teacher</div>

&#x20;           </div>

&#x20;           <div class="cv-body" id="splitSchoolBody">

&#x20;               @body

&#x20;           </div>

&#x20;           <div class="cv-foot" style="padding-top:20px">

&#x20;               <a class="" href="javascript:void(0);" id="splitSchoolUp">@pageup</a>

&#x20;               <span style="padding: 0 10px;">@pagetotal1 <span id="splitSchoolTotalPage">@totalPage</span> @pagetotal2 <span id="splitSchoolPageNumber">@pageNumber</span> @pagetotal3</span>

&#x20;               <a class="" href="javascript:void(0);" id="splitSchoolDown">@pagedown</a>

&#x20;           </div>

&#x20;       </div>

&#x20;   </script>

&#x20;   <!--分离的全校课程的列表每行的内容模板-->

&#x20;   <script type="text/template" id="tpl-splitSchool-list-row">

&#x20;       <div class="cv-row row-splitSchool-link">

&#x09;		<div class="cv-school-cz-col cv-setting-col @selectedClass">

&#x09;			<a href="javascript:void(0)" class="row-school-index" index="@index">@check</a>

&#x09;			<button class="cv-btn cv-tag">@volunteerText</button>

&#x09;			<a class="cv-choice @display @disable" extInfo="@extInfo" isConflict="@isConflict" retakeTypeDetail="@retakeTypeDetail" retakeType="@retakeType" limitGender="@limitGender" campus="@campus" teachCampus="@teachCampus" number="@number" tcId="@tcId" hasTest="@hasTest" isHasCj="@isHasCj" href="javascript:void(0);" @isDisabled>@xz</a>

&#x09;		</div>

&#x20;           <div class="cv-school-number-col">@allCourseNumber</div>

&#x20;           <div class="cv-school-title-col">

&#x09;			@courseName

&#x09;			<span class="cv-courseFlag @courseFlagDisplay">@courseFlag</span>

&#x09;		</div>

&#x09;		<div class="cv-normal cv-school-jxbid-col">@teachingClassID</div>

&#x09;		<div class="cv-school-time-col" title="@timeTitle">@time</div>

&#x09;		<div class="cv-school-examTime-col">@examTime</div>

&#x09;		<div class="cv-school-campus-col">@campusName</div>

&#x20;           <div class="cv-school-department-col">@departmentName</div>

&#x20;           <div class="cv-school-coursegroup-col">@courseGroupName</div>

&#x20;           <div class="cv-school-nature-col">@courseNatureName</div>

&#x20;           <div class="cv-school-type-col">@courseTypeName</div>

&#x09;		<div class="cv-school-rwxdlx-col">@rwxdlx</div>

&#x09;		<div class="cv-school-xgxklb-col">@type<br/>@courseSection</div>

&#x09;		<div class="cv-school-sfmooc-col">@isMooc</div>

&#x09;		<div class="cv-school-skyz-col">@teachLanguage</div>

&#x09;		<div class="cv-school-capcity-col">@capcity</div>

&#x20;           <div class="cv-school-credit-col">@credit</div>

&#x20;           <div class="cv-school-examTypeName-col">@examTypeName</div>

&#x20;           <div class="cv-school-teacher-col">@teacherName</div>

&#x20;       </div>

&#x20;   </script>



&#x20;   <!-- 侧边栏学生信息模板 -->

&#x09;<script type="text/template" id="tpl-stundent-information">        

&#x20;       <div class="cv-clearfix-child">

&#x20;           <!--用户头像-->

&#x20;           <div class="cv-user-info-img">

&#x20;               <img src="@headImageUrl">

&#x20;           </div>

&#x20;           <!--个人信息详情-->

&#x20;           <div class="cv-user-info-option">

&#x20;               <h5 class="cv-mb-8">@welcome

&#x20;                   <span>@name</span>

&#x20;               </h5>

&#x20;               <div class="cv-mb-4">@college/@department</div>

&#x20;               <div>@grade</div>

&#x20;           </div>

&#x20;       </div>

&#x20;       <!--图表部分-->

&#x20;       <div class="cv-credit-chart">

&#x20;           <!--所修学分占比-->

&#x20;           <!--<div>@getCreditProportion</div>-->

&#x20;           <!--图表初始化占位-->

&#x20;           <canvas id="cvCreditChart"></canvas>

&#x20;       </div>

&#x20;       <!--学分情况部分-->

&#x20;       <div id="cvCreditInfo" class="cv-credit-info cv-clearfix-child cv-mb-8">

&#x20;           <div>

&#x20;               <div class="cv-credit-num">@totalCredit</div>

&#x20;               <div class="cv-credit-caption">总学分</div>

&#x20;               <div class="cv-credit-color cv-all"></div>

&#x20;           </div>



&#x20;           <div>

&#x20;               <div class="cv-credit-num">@needCredit</div>

&#x20;               <div class="cv-credit-caption">已选学分</div>

&#x20;               <div class="cv-credit-color cv-not"></div>

&#x20;           </div>

&#x20;       </div>

&#x20;       <!--进入选课按钮-->

&#x20;       <button class="cv-btn cv-ghost cv-mb-8 cv-select" type="button" id="changeCampus" code="@code">@campusName</button>

&#x09;</script>



&#x20;   <!-- 侧边栏 - 学生落选结果 -->

&#x20;   <script type="text/template" id="tpl-stundent-unsuccessful">

&#x20;       <div style="height:100%"> 

&#x20;           <h5>落选课程</h5>

&#x20;           <div class="cv-list">

&#x20;               <div class="cv-head">

&#x20;                   <div class="cv-normal" style="width:20%">@time</div>

&#x20;                   <div class="cv-normal" style="width:40%">@kcm</div>

&#x20;                   <div class="cv-normal" style="width:20%">@teacher</div>

&#x20;                   <div class="cv-normal" style="width:20%">@courseresult</div>

&#x20;               </div>

&#x20;               <div class="cv-body">

&#x20;                   @body

&#x20;               </div>

&#x20;           </div>    

&#x20;       </div>

&#x20;   </script>



&#x20;   <script type="text/template" id="tpl-stundent-unsuccessful-row">

&#x20;       <div class="cv-row">

&#x20;           <div class="cv-normal" style="width:20%">@date</div>

&#x20;           <div class="cv-normal" style="width:40%">@courseName</div>

&#x20;           <div class="cv-normal" style="width:20%">@teacherName</div>

&#x20;           <div class="cv-normal" style="width:20%">@result</div>

&#x20;       </div>

&#x20;   </script>

&#x20;   

&#x20;   <!--教学班详情模板-->

&#x20;   <script type="text/template" id="tpl-jxbDetail-model">

&#x20;       <div class="cv-jxbdatail">

&#x20;           <div class="title">@jsTitle</div>

&#x09;		<div class="jsxx">@jsxx</div>

&#x09;		<div class="title">@tjbjTitle</div>

&#x09;		<div class="tjbjxx">@tjbjxx</div>

&#x09;		<div class="title">@jxbTitle</div>

&#x09;		<div class="jxbxx">@jxbxx</div>

&#x09;		<div class="title" style="display: @display">@kssjTitle</div>

&#x09;		<div class="kssj" style="display: @display">@kssj</div>

&#x09;		<div class="title" style="display: @courseDisplay"><a class="" target="\_blank" href="@courseUrl">@kcdetail</a></div>

&#x09;		<div class="kssj" style="display: @courseDisplay"><a class="" target="\_blank" href="@courseUrl">@jxdg</a></div>

&#x20;       </div>

&#x20;   </script>



&#x20;   <!-- 实验课程表格模板 -->

&#x20;   <script type="text/template" id="tpl-test-course-table">

&#x20;       <div class="table syk-table">

&#x20;           <h2>@theoryClassInfo</h2>

&#x20;           <p>@theoryClassTeachingPlace</p>

&#x09;		<div class="extInfo">@extInfo</div>

&#x09;		<div class="table-container">

&#x20;           	<table>

&#x20;              	 	<thead>

&#x20;                  	 	<tr>

&#x20;                       	<th style="width:40px;">操作</th>

&#x20;                       	<th style="width:60px;">班号</th>

&#x20;                      	 	<th style="width:100px;">上课教师</th>

&#x20;                       	<th>时间地点</th>

&#x09;						<th style="width:100px;">选课说明</th>

&#x20;                       	<th style="width:70px;">已选人数</th>

&#x20;                       	<th style="width:70px;">课容量</th>                      

&#x20;                       	<th style="width:100px;">不可选原因</th>                      

&#x20;                   	</tr>

&#x20;               	</thead>

&#x20;               	<tbody>@tbody</tbody>

&#x20;           	</table>

&#x09;		</div>

&#x20;           <a class="cv-btn cv-btn-chose" href="#" id="testCourse\_choice\_btn">选择</a>

&#x20;       </div>

&#x20;   </script>

&#x20;   <script type="text/template" id="tpl-test-course-table-row">

&#x20;       <tr>

&#x20;           <td>@radioHtml</td>

&#x20;           <td><span>@teachingClassID</span></td>

&#x20;           <td><span>@teacher</span></td>

&#x20;           <td><span>@teachingPlace</span></td>

&#x09;		<td><span>@extInfo</span></td>

&#x20;           <td><span>@numberOfSelected</span></td>

&#x20;           <td><span>@remainingCapacity</span></td>

&#x20;           <td><span>@cannotSelectReason</span></td>

&#x20;       </tr>

&#x20;   </script>



&#x20;   <script type="text/template" id="tpl-schoolcourse-view">

&#x20;       <div class="schoolcourse-view-table">

&#x09;		<h2>@courseTitle</h2>

&#x09;		<h4>@yyfx</h4>

&#x09;		<div>

&#x09;			@chooseBody

&#x09;		</div>

&#x20;           <h4>@jxbdetail</h4>

&#x20;           <table class="table-all">

&#x20;               <tr>

&#x20;                   <td>@kkdw</td>

&#x20;                   <td>@departmentName</td>

&#x20;               </tr>

&#x20;               <tr>

&#x20;                   <td>@campus</td>

&#x20;                   <td>@campusName</td>

&#x20;               </tr>

&#x20;               <tr>

&#x20;                   <td>@kcxz</td>

&#x20;                   <td>@courseNatureName</td>

&#x20;               </tr>

&#x20;               <tr>

&#x20;                   <td>@kclb</td>

&#x20;                   <td>@courseTypeName</td>

&#x20;               </tr>

&#x20;               <tr>

&#x20;                   <td>@xfxs</td>

&#x20;                   <td>@credit@xfTitle/@hours@xsTitle</td>

&#x20;               </tr>

&#x20;               <tr>

&#x20;                   <td>@teacher</td>

&#x20;                   <td>@teacherName</td>

&#x20;               </tr>

&#x20;               <tr>

&#x20;                   <td>@timeplace</td>

&#x20;                   <td>@teachingPlace</td>

&#x20;               </tr>

&#x20;               <tr>

&#x20;                   <td>@mxbj</td>

&#x20;                   <td>@scStr</td>

&#x20;               </tr>

&#x20;               <tr>

&#x20;                   <td>@xzxx</td>

&#x20;                   <td>@lkStr</td>

&#x20;               </tr>

&#x20;               <tr>

&#x20;                   <td>@xksm</td>

&#x20;                   <td>@extInfo</td>

&#x20;               </tr>

&#x20;           </table>

&#x20;       </div>

&#x20;   </script>

&#x20;   

&#x20;   <script type="text/template" id="electiveBatch\_list\_select">

&#x09;	<div class="xzlc-container electiveBatch">

&#x09;		<div class="lc-container">

&#x09;        	<table class="electiveBatch-list-table" cellspacing="0">

&#x09;				<thead class="electiveBatch-head">

&#x09;            		<th class="cv-electiveBatch-operate">@operate</th>

&#x09;            		<th class="cv-electiveBatch-name">@name</th>

&#x09;					<th class="cv-electiveBatch-kssj">@begintime</th>

&#x09;					<th class="cv-electiveBatch-jssj">@endtime</th>

&#x09;					<th class="cv-electiveBatch-sfkkxq">@crossCampus</th>

&#x09;					<th class="cv-electiveBatch-sfkct">@conflict</th>

&#x09;            		<th class="cv-electiveBatch-cause">@noSelectReason</th>

&#x09;				</thead>

&#x09;				<tbody class="electiveBatch-body">@electiveBatchBody</tbody>

&#x09;        	</table>

&#x09;		</div>

&#x09;		<div class="electiveBatchXznr @electiveBatchDisplay">

&#x09;			<div class="xznr-title">轮次须知</div>

&#x09;			<div class="xznr-content" style="margin-top: 5px;">

&#x09;				@confirmInfo

&#x09;			</div>

&#x09;			<div class="tyxz">

&#x09;				<span class="xydjs">

&#x09;					<span class="cv-color-grey-2">倒计时:</span>

&#x09;					<span class="cv-color-warning time"></span>

&#x09;				</span>

&#x09;				<label for="tyxz-input" class="tyxz-container">

&#x09;					<input id="tyxz-input" type="checkbox" name="tyxz" value="" />已阅读须知，并同意

&#x09;				</label>

&#x09;			</div>

&#x09;		</div>

&#x09;	</div>

&#x20;   </script>

&#x20;   <script type="text/template" id="expElectiveBatch\_list\_select">

&#x09;	<div class="xzlc-container expElectiveBatch">

&#x09;		<div class="lc-container">

&#x09;			<div style="width:100%;font-weight:bold;padding:5px 0px;">@sykxklc</div>

&#x09;        	<table class="electiveBatch-list-table" cellspacing="0">

&#x09;				<thead class="electiveBatch-head">

&#x09;            		<th class="cv-electiveBatch-operate">@operate</th>

&#x09;            		<th class="cv-electiveBatch-name">@name</th>

&#x09;            		<th class="cv-electiveBatch-kssj">@begintime</th>

&#x09;					<th class="cv-electiveBatch-jssj">@endtime</th>

&#x09;					<th class="cv-electiveBatch-sfkkxq">@crossCampus</th>

&#x09;					<th class="cv-electiveBatch-sfkct">@conflict</th>

&#x09;					<th class="cv-electiveBatch-cause">@internal</th>

&#x09;				</thead>

&#x09;				<tbody class="electiveBatch-body">@expElectiveBatchBody</tbody>

&#x09;        	</table>

&#x09;		</div>

&#x09;	</div>

&#x09;</script>

&#x20;   <script type="text/template" id="message\_queue\_list">

&#x09;	<div class="queue-container">

&#x20;       	<table class="queue-list-table" cellspacing="0">

&#x09;			<thead class="queue-head">

&#x20;           		<th class="cv-queue-state">状态</th>

&#x20;           		<th class="cv-queue-czlx">操作类型</th>

&#x20;           		<th class="cv-queue-kch">课程号</th>

&#x20;           		<th class="cv-queue-kcm">课程名称</th>

&#x20;           		<th class="cv-queue-kxh">班号</th>

&#x20;           		<th class="cv-queue-skjs">上课教师</th>

&#x20;           		<th class="cv-queue-sksj">上课时间</th>

&#x20;           		<th class="cv-queue-kclb">课程类别</th>

&#x20;           		<th class="cv-queue-kcxz">课程性质</th>

&#x20;           		<th class="cv-queue-xf">学分</th>

&#x09;			</thead>

&#x09;			<tbody class="queue-body">@queueBody</tbody>

&#x20;       	</table>

&#x09;	</div>

&#x20;   </script>

&#x20;   <script type="text/template" id="message\_queue\_list\_row">

&#x09;	<tr class="queue-row">

&#x20;      		<td class="cv-queue-state">@state</td>

&#x20;      		<td class="cv-queue-czlx">@czlx</td>

&#x20;      		<td class="cv-queue-kch">@kch</td>

&#x20;      		<td class="cv-queue-kcm">@kcm</td>

&#x20;      		<td class="cv-queue-kxh">@kxh</td>

&#x20;      		<td class="cv-queue-skjs">@skjs</td>

&#x20;      		<td class="cv-queue-sksj">@sksj</td>

&#x20;      		<td class="cv-queue-kclb">@kclb</td>

&#x20;      		<td class="cv-queue-kcxz">@kcxz</td>

&#x20;      		<td class="cv-queue-xf">@xf</td>

&#x09;	</tr>

&#x20;   </script>



&#x20;   <script type="text/javascript">

&#x20;       var BaseUrl = "https://jwxk.jnu.edu.cn/xsxkapp";

&#x20;       var length = BaseUrl.length;

&#x20;       if(BaseUrl.indexOf(length - 1, length) == '/') {

&#x20;           BaseUrl = BaseUrl.substring(0, length - 1);

&#x20;       }

&#x20;       

&#x20;       var uid = '2023101496';

&#x20;  		var loginType = 'cas';

&#x09;	var casUrl = 'https://icas.jnu.edu.cn/cas/login?service=https://jwxk.jnu.edu.cn/';

&#x09;	var casUrlOut = 'https://jwxk.jnu.edu.cn/xsxkapp/sys/xsxkapp/\*default/index.do';

&#x09;	var resUrl = 'https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp';

&#x20;       var socketUrl = 'null';

&#x20;       var pageType = 'grablessons';

&#x20;   </script>

&#x09;<script type='text/javascript' src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/plugins/jquery-3.4.1.min.js?av=1781150761398"></script>

&#x09;<script type="text/javascript" src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/plugins/i18n/jquery.i18n.properties.js?av=1781150761398"></script>

&#x20;   <script type='text/javascript' src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/js/jqxwidget/jquery.nicescroll.min.js?av=1781150761398"></script>

&#x20;   <script type='text/javascript' src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/js/jqxcore.js?av=1781150761398"></script>

&#x20;   <script type='text/javascript' src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/js/jqxtabs.js?av=1781150761398"></script>

&#x20;   <script type='text/javascript' src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/js/jqxwindow.js?av=1781150761398"></script>



&#x09;<script type="text/javascript" src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/js/bh\_utils.js?av=1781150761398"></script>

&#x09;<script type="text/javascript" src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/plugins/sortable/Sortable-1.3.0.js?av=1781150761398"></script>

&#x09;<script type="text/javascript" src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/js/xfimage.js?av=1781150761398"></script>

&#x09;<script type='text/javascript' src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/js/bhTip.js?av=1781150761398"></script>



&#x20;   <script type="text/javascript" src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/js/loginInUserRegister.js?av=1781150761398"></script>

&#x09;<script type="text/javascript" src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/js/index/indexBS.js?av=1781150761398"></script>

&#x09;<script type='text/javascript' src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/js/xsxkpub.js?av=1781150761398"></script>

&#x20;   <script type="text/javascript" src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/js/grablessons/grablessons.js?av=1781150761398"></script>

&#x09;<script type="text/javascript" src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/js/curriculavariable/sidebar.js?av=1781150761398"></script>

&#x09;<script type="text/javascript" src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/js/grablessons/grablessonsBS.js?av=1781150761398"></script>



&#x20;   <script type='text/javascript' src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/js/departurelog/departurelog.js?av=1781150761398"></script>

&#x20;   <script type='text/javascript' src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/js/departurelog/departurelogBS.js?av=1781150761398"></script>



&#x20;   <script type='text/javascript' src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/js/selectedcourse/selectedcourse.js?av=1781150761398"></script>

&#x20;   <script type='text/javascript' src="https://jwxkres.jnu.edu.cn/products/jwfw/xsxkapp/public/js/selectedcourse/selectedcourseBS.js?av=1781150761398"></script>

&#x20;   

&#x20;   <iframe id='iflogout' src='' style='display:none;' />

</body>

</html>

