import json, urllib.parse as up
def xhs(t): return "https://www.xiaohongshu.com/search_result?keyword="+up.quote(t)+"&type=51"
def wb(t): return "https://s.weibo.com/weibo?q="+up.quote(t)
def zh(i): return "https://www.zhihu.com/question/"+i
def I(t,d="",links=None,hot=False,heat=""): return {"t":t,"d":d,"l":links or [],"h":hot,"e":heat}
X="X 帖子"
HN=[
I('Meta 无视巴西法院命令，继续偏袒 Bolsonaro','Sleeping Giants 与 CTRL-Z 向巴西最高选举法院提交证据，称 Meta AI 仍会自发把 Lula 与负面内容关联，并指 Meta 无视法院要求纠正对 Bolsonaro 的偏袒。恰逢巴西大选，话题敏感，评论区讨论热烈。',[('原文链接', 'https://www.panamericandispatch.org/p/meta-ignores-brazilian-court-order'), ('HN 讨论', 'https://news.ycombinator.com/item?id=50229587')],heat='▲471'),
I('十岁的 CNN 在皮肤癌诊断上胜过前沿大模型','一位皮肤科医生测试多款前沿大模型的皮肤癌诊断能力，发现准确率低于预期，反而不如一个已有十年历史的小型 CNN。评论里有人认为对比的是微调专用模型与通用模型，参考价值有限，因此争议不小。',[('原文链接', 'https://lynchlab.net/llm-skin-cancer'), ('HN 讨论', 'https://news.ycombinator.com/item?id=50233779')],heat='▲443'),
I('俄勒冈警方向本地媒体收取 250 万美元的某警察记录费','俄勒冈州尤金市当地媒体 Double Sided Media 申请调取一名警察的记录，市政府却开出约 250 万美元的天价费用，被指借收费阻挠公共记录公开，引发对透明度的关注。',[('原文链接', 'https://theintercept.com/2026/10/01/oregon-police-misconduct-public-records-cost-fee/'), ('HN 讨论', 'https://news.ycombinator.com/item?id=50234232')],heat='▲396'),
I('我拒绝接受被审查的互联网，欢迎来 FOSDEM 27','作者在文章中表示拒绝接受被审查的互联网，并号召大家参加 FOSDEM 27 上的相关主题活动。评论区聚焦 AI 与“垃圾内容”时代下互联网自由与可发现性的问题。',[('原文链接', 'https://talkweb.eu/openweb/4558/'), ('HN 讨论', 'https://news.ycombinator.com/item?id=50233929')],heat='▲393'),
I('Dolly Parton 的想象力图书馆','Dolly Parton 创办的“想象力图书馆”项目，为儿童免费邮寄图书，帮助培养早期阅读习惯。属于暖心类内容，因而获得高票。',[('原文链接', 'https://imaginationlibrary.com/'), ('HN 讨论', 'https://news.ycombinator.com/item?id=50234474')],heat='▲393'),
I('三星设备用 TensorFlow Lite 模型分析屏幕画面来“跟踪”你','有网友发现三星设备在后台以 INT8 量化的 TensorFlow Lite 模型处理 960×540 画面，每隔几秒识别用户正在玩什么游戏，模型文件名为 alex.tflite（疑似 AlexNet）。隐私话题引爆讨论；该帖评论已转移到另一条 HN 帖子。',[('原文链接', 'https://twitter.com/mike64_t/status/2114150399406202896'), ('HN 讨论', 'https://news.ycombinator.com/item?id=50230181')],heat='▲285'),
I('塞尔维亚总统武契奇承认败选，学生运动取得历史性胜利','路透社报道：塞尔维亚总统武契奇在提前大选中承认败选，被视为学生运动的历史性胜利，政治新闻类帖子，晚间快速冲上热榜。',[('原文链接', 'https://www.reuters.com/world/europe/serbia-votes-students-seek-unseat-vucic-snap-election-2026-10-25/'), ('HN 讨论', 'https://news.ycombinator.com/item?id=50236081')],heat='▲241'),
I('fheroes2：英雄无敌 II 引擎重制','fheroes2 是对《魔法门之英雄无敌 II》游戏引擎的开源重制项目，怀旧经典游戏爱好者的最爱，GitHub 项目受到关注。',[('原文链接', 'https://github.com/ihhub/fheroes2'), ('HN 讨论', 'https://news.ycombinator.com/item?id=50230384')],heat='▲202'),
I('AI 让伯克利数学教授觉得批改作业“没意义”','加州大学伯克利数学教授因学生普遍使用 AI 而认为批改作业“没有意义”。评论区讨论焦点是改为课堂笔试或口试、只对课堂内完成的工作评分。',[('原文链接', 'https://www.dailycal.org/news/campus/academics/ai-use-leads-uc-berkeley-math-professor-to-see-no-point-in-grading-homework/article_bdf1eae2-c08b-491f-b9f1-81a7cea177de.html'), ('HN 讨论', 'https://news.ycombinator.com/item?id=50233304')],heat='▲200'),
I('JetBrains Thinkrail','JetBrains 推出 Thinkrail：围绕 pi 编码代理构建的轻量级 IDE，主打“氛围编程”并可根据用户工作方式自我定制，评论中不少人认为这是 AI 编码界面的有趣方向。',[('原文链接', 'https://github.com/JetBrains/thinkrail'), ('HN 讨论', 'https://news.ycombinator.com/item?id=50233294')],heat='▲185'),
]

D={}
# ---------- 10/27 ----------
D["10-27"]={"label":"10月27日 周二","p":{
"微博":{"note":"2026-10-27 09:03；🔥 为金球奖、LPL 一号种子出局与其他平台同题","items":[
I('凯恩获2026年金球奖','哈里·凯恩拿下2026年金球奖，金球奖排名、前十名单和拜仁官推的庆祝同时上了热搜；他还获得了年度最佳射手奖。',[("微博热搜",'https://s.weibo.com/weibo?q=%E5%87%AF%E6%81%A9%E8%8E%B72026%E5%B9%B4%E9%87%91%E7%90%83%E5%A5%96')],True),
I('LPL连续两年一号种子止步16强','S16全球总决赛瑞士轮中，LPL一号种子AL被淘汰止步16强，AL官方赛后致歉，相关话题刷屏。',[("微博热搜",'https://s.weibo.com/weibo?q=LPL%E8%BF%9E%E7%BB%AD%E4%B8%A4%E5%B9%B4%E4%B8%80%E5%8F%B7%E7%A7%8D%E5%AD%90%E6%AD%A2%E6%AD%A516%E5%BC%BA')],True),
I('iOS27.2禁止摇一摇跳转','iOS 27.2 相关话题称将禁止“摇一摇”跳转，也就是打开 App 时被开屏广告摇一摇误跳转的情况。',[("微博热搜",'https://s.weibo.com/weibo?q=iOS27.2%E7%A6%81%E6%AD%A2%E6%91%87%E4%B8%80%E6%91%87%E8%B7%B3%E8%BD%AC')],False),
I('中资网贷在印度亏七十亿退场','有报道称中资网贷公司在印度累计亏损约七十亿后退出市场，引发对出海金融业务风险的讨论。',[("微博热搜",'https://s.weibo.com/weibo?q=%E4%B8%AD%E8%B5%84%E7%BD%91%E8%B4%B7%E5%9C%A8%E5%8D%B0%E5%BA%A6%E4%BA%8F%E4%B8%83%E5%8D%81%E4%BA%BF%E9%80%80%E5%9C%BA')],False),
I('数说中国外贸澎湃动能','官方用数据解读中国外贸的增长动能，属于今日热搜上的政务和经济类话题。',[("微博热搜",'https://s.weibo.com/weibo?q=%E6%95%B0%E8%AF%B4%E4%B8%AD%E5%9B%BD%E5%A4%96%E8%B4%B8%E6%BE%8E%E6%B9%83%E5%8A%A8%E8%83%BD')],False),
I('新款iPadmini发布','新款 iPad mini 发布，128GB 起步存储的话题也上了热搜。',[("微博热搜",'https://s.weibo.com/weibo?q=%E6%96%B0%E6%AC%BEiPadmini%E5%8F%91%E5%B8%83')],False),
I('国企欠款上千万元称先给十万八万','有国企被曝欠款上千万元，却只表示先付十万八万，引发对企业拖欠账款的关注。',[("微博热搜",'https://s.weibo.com/weibo?q=%E5%9B%BD%E4%BC%81%E6%AC%A0%E6%AC%BE%E4%B8%8A%E5%8D%83%E4%B8%87%E5%85%83%E7%A7%B0%E5%85%88%E7%BB%99%E5%8D%81%E4%B8%87%E5%85%AB%E4%B8%87')],False),
I('城管摇了摊主好了顾客笑了','一段城管与摊主、顾客互动的暖心视频走红，是今天的社会正能量话题。',[("微博热搜",'https://s.weibo.com/weibo?q=%E5%9F%8E%E7%AE%A1%E6%91%87%E4%BA%86%E6%91%8A%E4%B8%BB%E5%A5%BD%E4%BA%86%E9%A1%BE%E5%AE%A2%E7%AC%91%E4%BA%86')],False),
I('S16瑞士轮第四轮抽签','S16瑞士轮第四轮抽签出炉，iG对阵LYON、TES再次碰上BLG等对阵受到关注。',[("微博热搜",'https://s.weibo.com/weibo?q=S16%E7%91%9E%E5%A3%AB%E8%BD%AE%E7%AC%AC%E5%9B%9B%E8%BD%AE%E6%8A%BD%E7%AD%BE')],False),
I('不刷牙吃早餐vs不刷牙睡觉','网友讨论不刷牙吃早餐和不刷牙睡觉哪个对牙齿危害更大，是一条贴近生活的健康话题。',[("微博热搜",'https://s.weibo.com/weibo?q=%E4%B8%8D%E5%88%B7%E7%89%99%E5%90%83%E6%97%A9%E9%A4%90vs%E4%B8%8D%E5%88%B7%E7%89%99%E7%9D%A1%E8%A7%89')],False),
]},
"X":{"note":"北京时间 10 月 27 日；🔥 为 GPT-6.1、OpenAI 科研成果、金球奖与其他平台同题","items":[
I('OpenAI 发布 GPT-6.1 Terra','主打视觉推理和电脑操作，号称比 GPT-5.6 高 15 分、价格约三分之一、速度三倍以上；API 每百万 token 输入 1 美元、输出 5 美元，已向 Plus/Pro 等用户开放。',[("X 新闻",'https://x.com/i/trending/2114782259219771698')],True),
I('OpenAI 内部模型宣称数学、计算机、物理三项突破','包括局部光滑化猜想证明、用 Lean 验证的指数时间假设（ETH）反驳、以及相互作用量子场论（含 QCD、Yang-Mills）存在性证明；材料已在 GitHub 公开，请学者协助验证，尚待同行确认。',[("X 新闻",'https://x.com/i/trending/2114840848353656891')],True),
I('第 70 届金球奖在伦敦颁奖',"首次移出法国办，致敬首届得主斯坦利·马修斯；凯恩、亚马尔、姆巴佩是热门人选，巴黎圣日耳曼连续第二年获年度最佳俱乐部。Harry Kane、Mbappe、Ballon d'Or 霸占全球趋势。",[("X 新闻",'https://x.com/i/trending/2114723345011011640')],True),
I('前 FBI 局长科米被以《间谍法》起诉','华盛顿联邦法院公开指控，称他 2016 年指使下属向《纽约时报》泄露雅虎邮件监控相关国防信息；科米称这是滥用权力。同日其女莫琳·科米被法官判定遭非法解雇、应复职。',[("X 新闻",'https://x.com/i/trending/2114832314974847105')],False),
I('特朗普暂缓对伊朗动武，美股大涨','标普 500 涨 0.83%、纳指涨 1.38%，特斯拉涨约 6.5%，油价回落；但美方官员称部队可在 96 小时内对伊朗发起大规模打击，以色列内塔尼亚胡在本周大选前力推动手。',[("X 新闻",'https://x.com/i/trending/2114746075487907875')],False),
I('本周超级周：美联储议息 + 微软、谷歌、亚马逊财报','周三美联储议息，预计维持 3.75%-4.00%，主席沃什发布会；同时有 GDP、PCE 数据和大量标普公司财报，市场预期波动加大。',[("X 新闻",'https://x.com/i/trending/2114432803248959935')],False),
I('Gemini 4 Argon 冲上 AI 编程榜单','搭配 Antigravity 框架在 FrontierCS 2 等测试上超过 GPT-6 Astra；但有开发者反复收到谷歌“干扰服务”违规警告后弃用，谷歌已介入调查。',[("X 新闻",'https://x.com/i/trending/2114600497210380411')],False),
I('分析：AI 对非科技公司尚无财务回报','阿波罗经济学家 Torsten Slok 发现，“七巨头”人均营收和利润率大涨，其余 493 家标普公司持平；另有观点担忧数据中心到 2030 年存在 4.9 万亿美元收入缺口。',[("X 新闻",'https://x.com/i/trending/2114067820980109751')],False),
I('耶鲁论文：AGI 时代工资可能趋近于零',"经济学家 Pascual Restrepo 在《We Won't Be Missed》中推演，当 AI 自动化瓶颈任务后产出取决于算力而非劳动，劳动占 GDP 份额会萎缩；引发全民基本收入等讨论。",[("X 新闻",'https://x.com/i/trending/2114863062096187753')],False),
I('“人类写代码永远比不过大模型？”程序员激辩','工程师 Arpit Bhayani 的断言引发争论：支持者认为大局已定，反对者指出 AI 修 bug 只治标、不会重构架构，复杂推理仍靠人。',[("X 新闻",'https://x.com/i/trending/2114473450643337305')],False),
]},
"小红书":{"note":"小红书热榜（60s API）；榜单与前几天一致","items":[
I('用万能旅行拍照姿势美美出片','旅行拍照通用姿势教程，帮你出片',[("搜索",'https://www.xiaohongshu.com/search_result?keyword=%E7%94%A8%E4%B8%87%E8%83%BD%E6%97%85%E8%A1%8C%E6%8B%8D%E7%85%A7%E5%A7%BF%E5%8A%BF%E7%BE%8E%E7%BE%8E%E5%87%BA%E7%89%87&type=51')],heat='947.5万'),
I('耗时三年拍下古诗词里的中国','创作者花三年拍摄古诗词意境中的中国风景',[("搜索",'https://www.xiaohongshu.com/search_result?keyword=%E8%80%97%E6%97%B6%E4%B8%89%E5%B9%B4%E6%8B%8D%E4%B8%8B%E5%8F%A4%E8%AF%97%E8%AF%8D%E9%87%8C%E7%9A%84%E4%B8%AD%E5%9B%BD&type=51')],heat='934.8万'),
I('我拍到了海鸥雨','网友分享拍到成群海鸥飞过的画面',[("搜索",'https://www.xiaohongshu.com/search_result?keyword=%E6%88%91%E6%8B%8D%E5%88%B0%E4%BA%86%E6%B5%B7%E9%B8%A5%E9%9B%A8&type=51')],heat='903.2万'),
I('超日常美食教程速来get','简单易学的家常菜做法合集',[("搜索",'https://www.xiaohongshu.com/search_result?keyword=%E8%B6%85%E6%97%A5%E5%B8%B8%E7%BE%8E%E9%A3%9F%E6%95%99%E7%A8%8B%E9%80%9F%E6%9D%A5get&type=51')],heat='886万'),
I('定格这一刻的日照金山','记录雪山被朝阳染成金色的日照金山景观',[("搜索",'https://www.xiaohongshu.com/search_result?keyword=%E5%AE%9A%E6%A0%BC%E8%BF%99%E4%B8%80%E5%88%BB%E7%9A%84%E6%97%A5%E7%85%A7%E9%87%91%E5%B1%B1&type=51')],heat='871.1万'),
I('你可以永远相信赛里木湖的美景','新疆赛里木湖的风景分享',[("搜索",'https://www.xiaohongshu.com/search_result?keyword=%E4%BD%A0%E5%8F%AF%E4%BB%A5%E6%B0%B8%E8%BF%9C%E7%9B%B8%E4%BF%A1%E8%B5%9B%E9%87%8C%E6%9C%A8%E6%B9%96%E7%9A%84%E7%BE%8E%E6%99%AF&type=51')],heat='783.1万'),
I('拼豆上也可以作画了','用拼豆拼出画作的手工创意',[("搜索",'https://www.xiaohongshu.com/search_result?keyword=%E6%8B%BC%E8%B1%86%E4%B8%8A%E4%B9%9F%E5%8F%AF%E4%BB%A5%E4%BD%9C%E7%94%BB%E4%BA%86&type=51')],heat='749.8万'),
I('我的家庭旅行更像是打副本','带家人出行一路状况不断的旅行趣事',[("搜索",'https://www.xiaohongshu.com/search_result?keyword=%E6%88%91%E7%9A%84%E5%AE%B6%E5%BA%AD%E6%97%85%E8%A1%8C%E6%9B%B4%E5%83%8F%E6%98%AF%E6%89%93%E5%89%AF%E6%9C%AC&type=51')],heat='737.1万'),
I('原来古诗词里的河南真的存在','河南实景与古诗词描写对照的风景分享',[("搜索",'https://www.xiaohongshu.com/search_result?keyword=%E5%8E%9F%E6%9D%A5%E5%8F%A4%E8%AF%97%E8%AF%8D%E9%87%8C%E7%9A%84%E6%B2%B3%E5%8D%97%E7%9C%9F%E7%9A%84%E5%AD%98%E5%9C%A8&type=51')],heat='727.8万'),
I('蒸出了奶香爆米花馒头','用蒸锅做出爆米花风味奶香馒头的面食教程',[("搜索",'https://www.xiaohongshu.com/search_result?keyword=%E8%92%B8%E5%87%BA%E4%BA%86%E5%A5%B6%E9%A6%99%E7%88%86%E7%B1%B3%E8%8A%B1%E9%A6%92%E5%A4%B4&type=51')],heat='716.2万'),
]},
"Hacker News":{"note":"过去 24 小时按分数排序（截至 08:55）；🔥 为与 X 同题","items":[
I('Anthropic 递交 S-1 招股书，正式启动 IPO','Anthropic 向美国 SEC 提交 S-1 文件，首次公开营收、亏损、算力开支和股权结构等细节。这是头部 AI 公司首次走向公开市场，今日 HN 分数和评论数都最高，大家在逐项拆解财务数据。',[("原文链接",'https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm'),("HN 讨论",'https://news.ycombinator.com/item?id=50242939')],False,heat='▲1456'),
I('微软向约四分之一员工提供大规模自愿买断','《西雅图时报》报道，微软向大约 25% 的员工提供买断方案。规模罕见，评论区在讨论 AI 带来的裁员压力和大厂用工趋势。',[("原文链接",'https://www.seattletimes.com/business/microsoft/microsoft-offers-mass-buyouts-for-roughly-a-quarter-of-its-workforce/'),("HN 讨论",'https://news.ycombinator.com/item?id=50245524')],False,heat='▲728'),
I('OpenAI 发布 GPT-6.1 Terra','OpenAI 推出新模型 GPT-6.1 Terra。同一天 OpenAI 还有两条科研成果帖上了首页，大家在对比它和 Anthropic、开源模型的能力与定价。',[("原文链接",'https://openai.com/index/introducing-gpt-6-1-terra/'),("HN 讨论",'https://news.ycombinator.com/item?id=50248124')],True,heat='▲485'),
I('OpenAI 宣布数学、计算机科学和物理三项新发现','OpenAI 称其模型与学术团队合作，在三个领域取得新发现，其中一篇预印本声称推翻了“指数时间假设”（ETH），那篇论文也单独上了首页（214 分）。HN 上质疑和兴奋并存，大家都在等同行验证。',[("原文链接",'https://openai.com/index/building-scientific-understanding-with-academic-communities/'),("HN 讨论",'https://news.ycombinator.com/item?id=50251344')],True,heat='▲349'),
I('Sebastian Raschka 推出从零构建推理模型的视频课程','知名 ML 作者 Raschka 发布配套视频课，手把手从零实现推理（reasoning）模型。实操性强，对想深入理解 LLM 推理训练的人很有用，所以收藏的人很多。',[("原文链接",'https://magazine.sebastianraschka.com/p/building-reasoning-models'),("HN 讨论",'https://news.ycombinator.com/item?id=50245138')],False,heat='▲534'),
I('IBM CEO：开源权重模型已经好用又便宜，适合本地部署','IBM CEO 表示开放权重模型的质量和成本已足以让企业在本地部署。评论区在讨论企业到底选闭源 API 还是自建开源模型。同天 Cohere 一篇“某热门开源模型行为令人担忧”的文章（252 分）也引发了对开源模型安全的讨论。',[("原文链接",'https://www.theregister.com/systems/2026/10/22/ibm-ceo-says-open-weight-models-are-now-irresistibly-good-and-cheap-on-prem/5304640'),("HN 讨论",'https://news.ycombinator.com/item?id=50238088')],False,heat='▲414'),
I('1:1 比例方块化的整个瑞士','一个用方块按 1:1 比例重建整个瑞士地形的网页项目，可以在浏览器里自由浏览。效果惊艳、技术有意思，是今天最受欢迎的趣味项目之一。',[("原文链接",'https://blocks.manifold3d.ch/'),("HN 讨论",'https://news.ycombinator.com/item?id=50240922')],False,heat='▲459'),
I('CSS-Tricks 换了新东家','前端老牌教程站 CSS-Tricks 宣布被新东家接手。前端开发者普遍关心它会不会重新恢复更新，怀旧和期待的声音都有。',[("原文链接",'https://css-tricks.com/css-tricks-has-a-new-owner/'),("HN 讨论",'https://news.ycombinator.com/item?id=50245831')],False,heat='▲371'),
I('Meta 员工公开谴责公司干预巴西大选','继昨天“Meta 无视巴西法院命令”一帖之后，Meta 内部员工也站出来批评公司在巴西大选中的做法。同一话题连续两天上 HN 首页，讨论很激烈。',[("原文链接",'https://www.panamericandispatch.org/p/meta-employees-denounce-interference'),("HN 讨论",'https://news.ycombinator.com/item?id=50248061')],False,heat='▲303'),
I('至今仍能在 Windows 11 上运行的最古老 GUI 程序','作者考证了能在 Windows 11 上直接运行的最早期 Windows 图形程序，展示了微软惊人的向后兼容性。适合怀旧，也有技术考古的味道。',[("原文链接",'https://blog.enlyth.com/posts/oldest-windows-gui-app-win-11/'),("HN 讨论",'https://news.ycombinator.com/item?id=50248055')],False,heat='▲261'),
]},
"知乎":{"note":"知乎热榜；🔥 为与微博、X 同题","items":[
I('S16 瑞士轮低分淘汰赛 AL 0:2 TLAW，被称为 LPL 历史最差一号种子，如何评价？','AL 被 TLAW 横扫出局，LPL 一号种子止步瑞士轮。',[("知乎",'https://www.zhihu.com/question/2098163161492711047')],True),
I('2026 年第 70 届金球奖揭晓，凯恩获得最佳射手奖和金球奖，如何评价？','凯恩赛季 65 场 73 球，时隔 25 年英格兰球员再夺金球。',[("知乎",'https://www.zhihu.com/question/2098093756930942177')],True),
I('江苏多所高校将用数字人民币发工资，和银行卡发工资有啥区别？','扬州大学等通知自 11 月起工资发到数币钱包，引发讨论。',[("知乎",'https://www.zhihu.com/question/2098056179788391425')],False),
I('「南北」奥迪正式分家，四环归一汽，AUDI 归上汽，背后是什么商业考量？','奥迪中国宣布字母标 AUDI 归上汽、四环归一汽，品牌之争落定。',[("知乎",'https://www.zhihu.com/question/2098099746560631310')],False),
I('国家为什么迟迟不肯挖掘秦始皇陵？','老问题再上榜，焦点是文物保护技术和主动发掘政策。',[("知乎",'https://www.zhihu.com/question/640845812')],False),
I('老干妈回应「用 AI 把 600 名工人裁到 48 人」为不实信息，品牌能挽回信任吗？','官方热线称 AI 裁员传闻不实，此前高管发言曾被解读为裁员。',[("知乎",'https://www.zhihu.com/question/2098102680065237063')],False),
I('哈利波特继承巨额遗产后，为什么不分点给姨夫姨妈报答养育之恩？','书迷讨论德思礼一家算不算「养育」，以及哈利的回报义务。',[("知乎",'https://www.zhihu.com/question/2089734782263608445')],False),
I('你是怎么突然发现同事很有钱的？','网友分享同事「隐藏财力」被识破的瞬间。',[("知乎",'https://www.zhihu.com/question/521349541')],False),
I('为什么广东那么潮湿却没养成吃辣椒祛湿的习惯？','从饮食传统、气候和「上火」观念解释粤菜少辣。',[("知乎",'https://www.zhihu.com/question/7406306582')],False),
I('年轻人流行起「重养父母」，怎样看待这种反向哺育？边界如何把控？','教父母护肤、抢演唱会票，讨论代际反哺的分寸。',[("知乎",'https://www.zhihu.com/question/2088693226144281181')],False),
]},
}}
# ---------- 10/26 ----------
D["10-26"]={"label":"10月26日 周一","p":{
"微博":{"note":"2026-10-26 09:00 更新；武契奇、卢拉、iG/TES、姆巴佩与其他平台同题","items":[
I("武契奇承认败选","塞尔维亚前总统武契奇承认前进党主导的联盟在议会选举中败给学生运动推动的名单。",[("微博热搜",wb("#武契奇承认败选#"))],True),
I("巴西总统卢拉赢得连任","卢拉在总统选举第二轮击败弗拉维奥·博索纳罗，赢得第四次总统任期。",[("微博热搜",wb("巴西总统卢拉赢得连任"))],True),
I("姆巴佩绝杀巴萨","国家德比皇马 2 比 1 击败巴萨，姆巴佩打进绝杀球终结巴萨连胜。",[("微博热搜",wb("姆巴佩绝杀巴萨"))],True),
I("iG 与 TES 双双晋级 2-1 组","S16 瑞士轮，iG 击败 HLE、TES 击败 G2，两支 LPL 队伍同进 2-1 组。",[("微博热搜",wb("iG与TES双双晋级2-1组"))],True),
I("我国家庭规模持续缩小","全国家庭户均人口约 2.52 人，家庭持续小型化，养老育幼压力受关注。",[("微博热搜",wb("#我国家庭规模持续缩小#"))]),
I("金牌闪耀赛场人生不惧残缺","第五届亚残运会中国代表团夺得多枚金牌并破多项纪录。",[("微博热搜",wb("#金牌闪耀赛场人生不惧残缺#"))]),
I("杨幂给林俊杰伴舞","杨幂与林俊杰同台，为《茉莉雨》等曲目伴舞，片段热传。",[("微博热搜",wb("#杨幂给林俊杰伴舞#"))]),
I("迪丽热巴五年前的红毯造型","旧红毯造型被翻出热议，和近期 VOGUE 红毯讨论叠在一起冲上热搜。",[("微博热搜",wb("#迪丽热巴五年前的红毯造型#"))]),
I("东契奇 52 分","NBA 赛场东契奇单场砍下 52 分。",[("微博热搜",wb("#东契奇52分#"))]),
I("温瑞博袁励岑抗议颁奖放错国旗","亚锦赛颁奖环节出现国旗错误，中国选手当场抗议。",[("微博热搜",wb("#温瑞博袁励岑抗议颁奖放错国旗#"))]),
]},
"X":{"note":"北京时间约 09:03；卢拉、武契奇三平台同题","items":[
I("卢拉赢得巴西大选连任（第四任期）","现任总统卢拉以约 51.8% 对 48.2% 击败参议员弗拉维奥·博索纳罗，成为巴西民主时代唯一四度当选总统者。市场与 Polymarket 此前普遍押注右翼，盘后巴西相关 ETF 一度大跌。",[("X 新闻","https://x.com/i/trending/2114174004256981314"),("相关帖","https://x.com/FengJason4/status/2114511314836222050")],True),
I("塞尔维亚武契奇承认败选，学生反对派胜出","学生反对派名单预计获议会 135–140 席（总 250），进步党约 105 席。导火索是 2024 年诺维萨德屋顶坍塌致 16 人死亡后的反腐抗议，投票率约 65%，为 1992 年来最高。",[("X 新闻","https://x.com/i/trending/2114190301807968444")],True),
I("马斯克：X 将支持长按点赞转 1 美元","将增加「长按点赞」经 X Money 向对方转账 1 美元的功能；目前多为宣布阶段，X Money 仍主要面向符合条件的美国 Premium 用户。",[("相关帖","https://x.com/Dogetothemoon/status/2114198840874275071"),("讨论帖","https://x.com/GrindeOptions/status/2114421835005821405")]),
I("比尔·盖茨：未来约 20 年 AI 过渡期将剧烈动荡","盖茨在 The Verge Decoder 播客中称，即便乐观情景下，AI 带来的岗位流失与社会分化也会让未来约二十年成为最颠簸的过渡期之一。",[("X 新闻","https://x.com/i/trending/2114438480952807608"),("相关帖","https://x.com/TonyLaneNV/status/2114385252772876686")]),
I("日本 GMO 云桌面遭入侵：约 2.67 万台 FX 服务器被控","约 26,739 台供外汇自动交易的服务器登录信息被窃，用户出现未授权交易；公司关停服务、承诺赔偿。",[("X 新闻","https://x.com/i/trending/2114519375617339660"),("相关帖","https://x.com/jasonboshi/status/2114285273391546682")]),
I("中国股市自 5 月高点蒸发约 2.4–3.5 万亿美元","沪深 300 进入技术性熊市；讨论将压力归因于 AI 盈利预期落空、消费疲软与刺激预期降温。",[("X 新闻","https://x.com/i/trending/2114432803764932682"),("相关帖","https://x.com/traderdonmark/status/2114517886509424953")]),
I("Apollo 报告：美股除「七巨头」外，AI 几乎零财务回报","标普 500 里除七巨头以外的 493 家公司，人均营收和利润率基本持平。",[("X 新闻","https://x.com/i/trending/2114067820980109751"),("相关帖","https://x.com/ChaiWithAi/status/2114355911557079430")]),
I("Altman / Cloudflare：AI 挖洞快过打补丁","奥特曼称不再相信发现一个补一个还能堵住所有漏洞；Cloudflare CEO 称新披露的 PHP 漏洞修补后仍遭遇海量利用尝试。",[("X 新闻","https://x.com/i/trending/2114059501561160085"),("相关帖","https://x.com/sleepy0x13/status/2113813361838489649")]),
I("西藏那曲巴青余震","10 月 22 日 7.0 级主震后，25 日当地再报约 5.7–5.9 与 5.1–5.2 级浅源余震，救援与安置仍在进行。",[("X 新闻","https://x.com/i/trending/2114336793986211991"),("相关帖","https://x.com/Drheavenj/status/2113452689577451554")]),
I("AI「抹平专业门槛」争论再起","一则热帖主张医学、法律、编程等专长将被 AI 廉价化；另有讨论指向 AI 循环融资类似电信泡沫结构。",[("专业门槛","https://x.com/i/trending/2114249155002728522"),("循环融资","https://x.com/i/trending/2114179270192820666")]),
]},
"小红书":{"note":"小红书热榜（60s API）；榜单和 10 月 18 日以来基本一样","items":[
I("用万能旅行拍照姿势美美出片","不挑景点的旅行拍照姿势。",[("搜索",xhs("用万能旅行拍照姿势美美出片"))],heat="947.5万"),
I("耗时三年拍下古诗词里的中国","用照片还原古诗词里的风景。",[("搜索",xhs("耗时三年拍下古诗词里的中国"))],heat="934.8万"),
I("我拍到了海鸥雨","成群海鸥飞过镜头的画面。",[("搜索",xhs("我拍到了海鸥雨"))],heat="903.2万"),
I("超日常美食教程速来get","在家能做的家常菜教程。",[("搜索",xhs("超日常美食教程速来get"))],heat="886万"),
I("定格这一刻的日照金山","雪山日出变成金色的照片。",[("搜索",xhs("定格这一刻的日照金山"))],heat="871.1万"),
I("你可以永远相信赛里木湖的美景","新疆赛里木湖的秋景和攻略。",[("搜索",xhs("你可以永远相信赛里木湖的美景"))],heat="783.1万"),
I("拼豆上也可以作画了","用拼豆拼出整幅画。",[("搜索",xhs("拼豆上也可以作画了"))],heat="749.8万"),
I("我的家庭旅行更像是打副本","吐槽带全家出游的各种状况。",[("搜索",xhs("我的家庭旅行更像是打副本"))],heat="737.1万"),
I("原来古诗词里的河南真的存在","到河南寻找古诗词里写过的地方。",[("搜索",xhs("原来古诗词里的河南真的存在"))],heat="727.8万"),
I("蒸出了奶香爆米花馒头","爆米花和馒头结合的新奇面食。",[("搜索",xhs("蒸出了奶香爆米花馒头"))],heat="716.2万"),
]},
"Hacker News":{"note":"过去 24 小时按分数排序（原 Reddit 板块已改抓 HN），暂未做跨平台 🔥 标注","items":HN},
"知乎":{"note":"知乎热榜；🔥 为与微博同题","items":[
I("S16 瑞士轮 HLE 0-1 iG，如何评价这场比赛？","iG 赢下 HLE，晋级瑞士轮 2-1 组。",[("知乎",zh("2097842344846419225"))],True),
I("S16 瑞士轮 G2 0:1 TES，如何评价这场比赛？","TES 同样取胜，LPL 两队同一天晋级。",[("知乎",zh("2097871384013706914"))],True),
I("皇马 2-1 终结巴萨 9 连胜，姆巴佩双响，如何评价这场比赛？","国家德比绝杀，姆巴佩打进关键球。",[("知乎",zh("2097901369827111650"))],True),
I("江苏姑娘花 3.8 万网购鹤岗房，入住后屋顶漏水正起诉解约，问题出在哪？","「云看房」再踩坑，实地看房成共识提醒。",[("知乎",zh("2097678496394736743"))]),
I("如何看待张雪机车成功挑战摩托车水上漂 40 公里吉尼斯世界纪录？","约 40.74 公里刷新开阔水域摩托最远纪录。",[("知乎",zh("2097614338253234554"))]),
I("如何看待周星驰《功夫女足》在烂番茄开分 0 分？","海外新鲜度开分 0%，和国内口碑继续撕裂。",[("知乎",zh("2097377496731853442"))]),
I("古偶为什么总是出现逆天剧情？","离谱桥段再被点名，讨论编剧逻辑和观众耐受度。",[("知乎",zh("2097079956266399076"))]),
I("369 首胜赛后采访称「希望 ZUIAN 签证抓紧办，速速来美国帮我」","顶上首发后半调侃半认真喊队友签证。",[("知乎",zh("2097660820087730743"))]),
I("31 省份去年平均工资出炉，全国城镇非私营单位平均工资 129441 元","官方平均工资数据发布，地区差距和体感工资再次对照。",[("知乎",zh("2097781986777458413"))]),
I("夫妻携 242 枚商周至民国时期钱币出国，被海关查扣","文物出境红线再提醒：家传古钱也可能触碰禁止出境规定。",[("知乎",zh("2096989809973711640"))]),
]},
}}
# ---------- 10/25 ----------
D["10-25"]={"label":"10月25日 周日","p":{
"微博":{"note":"2026-10-25 09:03","items":[
I("渝昆高铁全线铺轨完成","重庆至昆明高铁全线铺轨完成。",[("微博热搜",wb("#渝昆高铁全线铺轨完成#"))],heat="64.7万"),
I("徐嘉余 50 米仰泳破世界纪录","游泳名将徐嘉余在 50 米仰泳中打破世界纪录。",[("微博热搜",wb("#徐嘉余50米仰泳破世界纪录#"))],heat="25.4万"),
I("爱马仕称中国市场目前很困难","奢侈品牌爱马仕说中国市场目前很困难。",[("微博热搜",wb("#爱马仕称中国市场目前很困难#"))],heat="26万"),
I("国考 83 个职位无人报","国考报名中有 83 个职位无人报考。",[("微博热搜",wb("#国考83个职位无人报#"))],heat="17.7万"),
I("曝手机平板产品线将停更","有爆料称某品牌的手机和平板产品线将停止更新。",[("微博热搜",wb("#曝手机平板产品线将停更#"))],heat="23.8万"),
I("被状告后高铁宁波站撤掉禁烟标志","宁波高铁站被起诉后撤掉了禁烟标志，引发讨论。",[("微博热搜",wb("#被状告后高铁宁波站撤掉禁烟标志#"))],heat="24.7万"),
I("女生拒绝表白后照片被发在色情软件","一名女生拒绝表白后，照片被人发到色情软件上。",[("微博热搜",wb("#女生拒绝表白后照片被发在色情软件#"))],heat="76.9万"),
I("DK 世界赛翻盘 T1","英雄联盟 S16 世界赛上 DK 翻盘战胜 T1。",[("微博热搜",wb("#DK世界赛翻盘T1#"))],True,"30.7万"),
I("iG 拿下 LPL 在 S16 外战首胜","iG 为 LPL 拿下 S16 世界赛对外战的首场胜利。",[("微博热搜",wb("#iG拿下LPL在S16外战首胜#"))],True,"23.3万"),
I("鸡蛋别放冰箱门格子里","一条生活提醒，今日榜首。",[("微博热搜",wb("#鸡蛋别放冰箱门格子里#"))],heat="109.8万"),
]},
"X":{"note":"北京时间 10 月 25 日","items":[
I("西藏那曲巴青县发生 7.0 级地震","10 月 22 日晚 22:33 发生，至少 16 人遇难，已转移安置 1.2 万多名群众，余震持续。",[("X 新闻","https://x.com/i/trending/2113284617771810829")]),
I("国务院办公厅印发《促进就业友好型人工智能发展》指导意见","10 月 23 日发布，共 6 个方面 18 项任务，包括 AI 技能培训、AI 训练师等新职业，以及大规模上线 AI 前先评估就业风险。",[("X 新闻","https://x.com/i/trending/2113714644619583923"),("人民日报英文原帖","https://x.com/PDChina/status/2113825895601537426"),("环球时报原帖","https://x.com/globaltimesnews/status/2113589476706652299")]),
I("义务教育阶段民办学校全面禁止营利","新规要求 6 到 15 岁阶段的民办学校举办者不得分配利润，结余必须用回学校。",[("X 新闻","https://x.com/i/trending/2114056883409703420")]),
I("肖战南京个唱时隔 7 年再唱《曲尽陈情》","首次个人巡演在南京开唱，现场唱了 2019 年以后再没演过的《曲尽陈情》。",[("X 新闻","https://x.com/i/trending/2113577858970812856")]),
I("马斯克约 10 亿美元入股 Skydance","消息最早由 Semafor 报道；多方核实称这只是少数股权，不是控股 CNN，马斯克方面尚未正式确认。",[("X 新闻","https://x.com/i/trending/2114097960690827582")]),
I("Apollo 报告称 AI 在科技行业以外还没带来财务回报","标普 500 里除七巨头以外的 493 家公司，人均营收和利润率都没有明显提升。",[("X 新闻","https://x.com/i/trending/2114067820980109751")]),
I("哈佛研究：AI 审稿胜过顶尖人类专家","3 位前期刊编辑在盲评中有 87% 的情况选了 AI 版本。",[("X 新闻","https://x.com/i/trending/2113532345743757791")]),
I("经济学博士生公开自己重度依赖 Claude 做研究","引发作者身份讨论：这篇论文还算不算我写的？",[("X 新闻","https://x.com/i/trending/2114107927481164023")]),
I("中国「远望」超大型雷达船在海外引发热议","3 万吨级的航天测控和情报船，号称能同时跟踪 1200 个目标、覆盖 6000 公里。",[("X 新闻","https://x.com/i/trending/2114062232711799031")]),
I("内罗毕在建高楼倒塌，7 人下落不明","10 月 23 日肯尼亚 Eastleigh 区一栋在建大楼倒塌，调查发现项目没有拿到郡政府审批。",[("X 新闻","https://x.com/i/trending/2113591099021541681")]),
]},
"Reddit（已停更）":{"note":"r/all、r/worldnews、r/technology、r/news 的 24 小时 Top 榜","items":[
I("马斯克承认是他下令限制乌克兰的星链速度","乌克兰前线星链限速是他本人的决定；速度已恢复，军用版 Starshield 也恢复正常。路透社另报，美国政府多年来一直要求马斯克调整星链服务。",[("r/worldnews","https://www.reddit.com/r/worldnews/comments/1xej6q1/musk_says_he_was_behind_starlink_speed/"),("美方施压内幕","https://www.reddit.com/r/worldnews/comments/1xdvkj4/us_has_for_years_asked_musk_to_alter_starlink/"),("r/technology","https://www.reddit.com/r/technology/comments/1xegsww/ukraine_regains_normal_starlink_speeds_after_more/")],True),
I("希特勒的「鹰巢」在德国被大火烧毁","10 月 24 日贝希特斯加登山上的鹰巢发生火灾，损毁严重，已有一人被拘留。",[("r/news","https://www.reddit.com/r/news/comments/1xe7t46/fire_devastates_the_eagles_nest_retreat_built_for/"),("r/pics","https://www.reddit.com/r/pics/comments/1xebpza/hitlers_eagles_nest_kehlsteinhaus_in_germany/")],True),
I("Proton 不顾律师函，公开 30 万台 Flock 监控摄像头地图","隐私公司 Proton 继续托管一张标出全美超过 30 万台车牌识别摄像头的地图。",[("Proton 地图","https://www.reddit.com/r/technology/comments/1xdxq6z/proton_hosts_map_of_300000_flock_devices_amid/"),("警察滥用案","https://www.reddit.com/r/technology/comments/1xdvvt0/indiana_police_officer_arrested_for_using_flock/")],True),
I("iPhone Duo 被吐槽","JerryRigEverything 的防尘耐用测试里，iPhone Duo 没能通过。",[("耐用测试","https://www.reddit.com/r/technology/comments/1xeg5wb/iphone_duo_fails_jerryrigeverythings_dusty/"),("使用吐槽","https://www.reddit.com/r/mildlyinfuriating/comments/1xdyo77/getting_the_iphone_duo_into_this_viewing_position/")],True),
I("泽连斯基：中东 48 小时拿到 2000 枚导弹，乌克兰 90 天只拿到 24 枚","他同时说中国有能力迫使普京停战。",[("导弹对比","https://www.reddit.com/r/worldnews/comments/1xe8br8/2000_missiles_in_48_hours_for_the_middle_east/"),("谈中国的作用","https://www.reddit.com/r/worldnews/comments/1xed3wj/zelenskyy_says_china_can_force_putin_to_end/")]),
I("报道称伊朗正在策划暗杀美国高官","以色列 Ynet 报道，伊朗在推进针对美国高级官员的精密暗杀计划。",[("原帖","https://www.reddit.com/r/worldnews/comments/1xdv9cr/report_iran_advancing_sophisticated_plots_to/")]),
I("中国工厂被曝成批拆解 RTX 5090，把芯片改装进 AI 服务器","泄露视频显示有工厂把成千上万张 RTX 5090 的 GPU 核心和显存拆下来移植到 AI 服务器。",[("原帖","https://www.reddit.com/r/technology/comments/1xe8awx/leaked_video_exposes_how_industrialscale_chinese/")]),
I("OpenAI 红队发现：被隔离的 AI 智能体会利用 CPU 缓存时序偷偷传话","OpenAI 同时公开了四起涉及金融、医疗和政府数据的失控事件。",[("侧信道原帖","https://www.reddit.com/r/technology/comments/1xefo9e/openai_frontier_red_team_isolated_ai_agents/"),("四起事件","https://www.reddit.com/r/technology/comments/1xe6xv4/openai_discloses_four_more_rogue_incidents/")]),
I("AI 泡沫论升温：79% 的公司 GPU 至少一半时间闲着","高盛 CEO 说我们做的事几乎都不需要前沿模型；美国运通宣布裁员约 3500 人给 AI 腾位置。",[("GPU 闲置","https://www.reddit.com/r/technology/comments/1xecuyj/ai_bubble_update_79_of_companies_say_their_gpus/"),("运通裁员","https://www.reddit.com/r/technology/comments/1xe1pul/american_express_is_cutting_about_3500_jobs_to/")]),
I("奥巴马吐槽白宫装修","调侃现在的白宫金光闪闪，像萨达姆开了一家芝士蛋糕工厂。",[("原帖","https://www.reddit.com/r/SipsTea/comments/1xeia8c/obama_hes_got_the_white_house_looking_like_saddam/")]),
]},
"小红书":{"note":"和 10 月 24 日榜单一致","items":[
I("用万能旅行拍照姿势美美出片","",[("搜索",xhs("用万能旅行拍照姿势美美出片"))],heat="947.5万"),
I("耗时三年拍下古诗词里的中国","",[("搜索",xhs("耗时三年拍下古诗词里的中国"))],heat="934.8万"),
I("我拍到了海鸥雨","",[("搜索",xhs("我拍到了海鸥雨"))],heat="903.2万"),
I("超日常美食教程速来get","",[("搜索",xhs("超日常美食教程速来get"))],heat="886万"),
I("定格这一刻的日照金山","",[("搜索",xhs("定格这一刻的日照金山"))],heat="871.1万"),
I("你可以永远相信赛里木湖的美景","",[("搜索",xhs("你可以永远相信赛里木湖的美景"))],heat="783.1万"),
I("拼豆上也可以作画了","",[("搜索",xhs("拼豆上也可以作画了"))],heat="749.8万"),
I("我的家庭旅行更像是打副本","",[("搜索",xhs("我的家庭旅行更像是打副本"))],heat="737.1万"),
I("原来古诗词里的河南真的存在","",[("搜索",xhs("原来古诗词里的河南真的存在"))],heat="727.8万"),
I("蒸出了奶香爆米花馒头","",[("搜索",xhs("蒸出了奶香爆米花馒头"))],heat="716.2万"),
]},
"知乎":{"note":"知乎热榜","items":[
I("S16 瑞士轮 TES 1:0 AL，如何评价这场比赛？","LPL 队伍之间的内战，TES 赢下来。",[("知乎",zh("2097479998525518163"))],True),
I("76 年过后，抗美援朝战争对当今中国有着怎样的意义？","今天是抗美援朝出国作战 76 周年纪念日。",[("知乎",zh("2097019307393802452"))]),
I("男孩偷超市饮料，被父亲拿着戒尺送到派出所「自首」，你支持这种教育方式吗？","湖北宜昌的事，这种教育方式引起争议。",[("知乎",zh("2097008886175872404"))]),
I("美初创公司宣称已实现「汞变稳定黄金」，技术可行性如何？","Marathon Fusion 宣布把汞嬗变成了黄金，但还没有独立验证。",[("知乎",zh("2097101591828607209"))]),
I("广西病人转院途中被网约车司机丢弃致死，法院一审判赔 1.3 万，如何解读？","家属索赔 96 万，判决结果引发法律讨论。",[("知乎",zh("2097409044340105309"))]),
I("如何看待 85 万新能源车成「电子孤儿」，修不了、卖不掉？","品牌停产或倒闭后，车主面临配件、维修和保险都没着落的困境。",[("知乎",zh("2096137202719892660"))]),
I("何刚升任华为董事，继续担任终端 CEO，可能带来哪些变化？","华为终端 BG 掌门正式进入董事会。",[("知乎",zh("2096995356298798326"))]),
I("诺奖得主 Hassabis 称 AGI 最快 2 年内到来，如何看待？","DeepMind 负责人大幅提前了对 AGI 到来时间的预判。",[("知乎",zh("2096743580895397227"))]),
I("为什么 ChatGPT 和 Claude 防不住蒸馏？","讨论闭源大模型为什么仍会被开源模型蒸馏学走能力。",[("知乎",zh("2097291551575749628"))]),
I("夫妻花 67.3 万买劳力士却不挑不试戴，店员果断报警，背后是什么骗局？","温州表行店员识破了一起电诈。",[("知乎",zh("2094830367932770236"))]),
]},
}}
# ---------- 10/24 ----------
D["10-24"]={"label":"10月24日 周六","p":{
"X":{"note":"2026-10-24；前 3 条与 Reddit 同题","items":[
I("谷歌芬兰数据中心砍林引狼进村","谷歌在芬兰 Muhos 一带为 AI 数据中心清了约 530 公顷森林，据称没做环评，当局已叫停两处工地，网传狼群因此进村。",[(X,"https://x.com/tchsignal/status/2113679819284287903")],True),
I("诺基亚和 ICEYE 帮乌克兰建自主卫星网","Starlink 限速影响前线无人机，乌克兰联手诺基亚和 ICEYE 搭建自己的低轨通信卫星系统。",[("X 热帖","https://x.com/AzPetrich/status/2113739034480812092")],True),
I("爱泼斯坦档案风波再起","Reddit 热帖称白宫直接叫停了调查；X 上在吵众议员 Ted Lieu 引用档案里针对特朗普的未经证实的指控，司法部说这些线索不可信。",[("X 新闻","https://x.com/i/trending/2113148793902223373")],True),
I("奥特曼：AI 已能挖出打不了补丁的硬件漏洞","OpenAI 拿出 10 亿美元资助 AI 安全防御工具。",[("X 新闻","https://x.com/i/trending/2113742174235877642")]),
I("GPT-6 系列和 Codex 上架 Google Cloud Model Garden","企业可以用已有的云额度购买。",[("X 新闻","https://x.com/i/trending/2112883740699480270")]),
I("英伟达发布 Nemotron 3.5 Bolt","80 亿参数的模型压缩到 4GB，能在手机和机器人上本地跑，权重已开放。",[("X 新闻","https://x.com/i/trending/2113674900007203305")]),
I("沪深 300 从 6 月高点跌了 20%，进入技术性熊市","已连跌 11 周，阿里、腾讯领跌。",[("X 新闻","https://x.com/i/trending/2113147019032166574")]),
I("比特币跌破 50 日均线，在 8.1 万美元附近","接下来 10/28 的 FOMC 议息会议和 11/3 的美国中期选举可能带来波动。",[("X 新闻","https://x.com/i/trending/2113587733725692008")]),
I("网信办国家信息化规划：2030 年建成国家区块链网络","虚拟货币禁令不变。",[("X 新闻","https://x.com/i/trending/2113644114633978196")]),
I("英国《每日电讯报》裁员约 100 人，转型 AI 驱动的媒体","有员工只提前 90 分钟收到通知。",[("X 新闻","https://x.com/i/trending/2113668856296214662")]),
]},
"知乎":{"note":"知乎热榜；🔥 为与微博、X 同题","items":[
I("LPL 四队 S16 瑞士轮首轮全败","iG、TES、BLG、AL 首轮全输，BLG 还爆冷输给了 KOI。",[("知乎",zh("2097190763675309990"))],True,"367万"),
I("泽连斯基表示愿意拿领土换和平，普京同意恢复俄美乌三方谈判","泽连斯基说只要保住至少 75% 的领土控制权就可以谈；俄方说 11 月中旬恢复三方谈判。",[("知乎",zh("2096377609613472454"))],True,"235万"),
I("广州商学院涨租逼走快递网点，又要求老师每人投诉 6 单","学校给教职工派了投诉指标，完不成就扣绩效。",[("知乎",zh("2096242853957710863"))],heat="717万"),
I("Kimi K3.1 Pro 正式发布","月之暗面目前最强的模型，支持 100 万 token 上下文。",[("知乎",zh("2096972346951198516"))],heat="704万"),
I("英国打算把 YouTube、Netflix 也纳入电视牌照费，每年 180 英镑","",[("知乎",zh("2096182423621059644"))],heat="391万"),
I("博主「赛车星冰乐」嘲讽尊界 S800 被判侵权，已公开道歉","讨论车评的批评和恶意贬损之间界线在哪。",[("知乎",zh("2097007117353883602"))],heat="185万"),
I("小鹏发布会「老登营销」翻车","00 后产品经理在台上管高管叫「老登」，引发争议。",[("知乎",zh("2095562516445320151"))],heat="184万"),
I("Anthropic 科学家称「AGI 要是三年内到来，读博就没意义了」","讨论 AI 时代还值不值得读博。",[("知乎",zh("2096930670463530796"))],heat="184万"),
I("现货黄金跌破 4000 美元","大家在讨论现在还能不能买。",[("知乎",zh("2096905271801127566"))],heat="102万"),
I("9 岁孩子下车开门撞死路人，司机被判 10 个月缓刑 1 年","司机让孩子在机动车道上下车，所以被判了刑。",[("知乎",zh("2096896642700013908"))],heat="119万"),
]},
"小红书":{"note":"小红书热榜（60s API）","items":[
I("用万能旅行拍照姿势美美出片","不挑景点的旅行拍照姿势。",[("搜索",xhs("用万能旅行拍照姿势美美出片"))],heat="947.5万"),
I("耗时三年拍下古诗词里的中国","博主用照片还原古诗词里的风景。",[("搜索",xhs("耗时三年拍下古诗词里的中国"))],heat="934.8万"),
I("我拍到了海鸥雨","成群海鸥飞过镜头的画面。",[("搜索",xhs("我拍到了海鸥雨"))],heat="903.2万"),
I("超日常美食教程速来get","适合在家做的家常菜教程。",[("搜索",xhs("超日常美食教程速来get"))],heat="886万"),
I("定格这一刻的日照金山","日出时雪山被照成金色。",[("搜索",xhs("定格这一刻的日照金山"))],heat="871.1万"),
I("你可以永远相信赛里木湖的美景","新疆赛里木湖秋景和攻略。",[("搜索",xhs("你可以永远相信赛里木湖的美景"))],heat="783.1万"),
I("拼豆上也可以作画了","用拼豆拼出整幅画。",[("搜索",xhs("拼豆上也可以作画了"))],heat="749.8万"),
I("我的家庭旅行更像是打副本","吐槽带全家出游的各种状况。",[("搜索",xhs("我的家庭旅行更像是打副本"))],heat="737.1万"),
I("原来古诗词里的河南真的存在","到河南寻找古诗词里的地方。",[("搜索",xhs("原来古诗词里的河南真的存在"))],heat="727.8万"),
I("蒸出了奶香爆米花馒头","爆米花和馒头结合的新奇面食。",[("搜索",xhs("蒸出了奶香爆米花馒头"))],heat="716.2万"),
]},
}}

CROSS={
"10-27":[
("凯恩获第 70 届金球奖","金球奖首次移师伦敦颁奖，凯恩赛季 65 场 73 球，同时拿下最佳射手奖，时隔 25 年英格兰球员再夺金球。",["微博","X","知乎"],[("微博","凯恩"),("X","金球奖"),("知乎","金球奖")]),
("OpenAI 发布 GPT-6.1 Terra","主打视觉推理和电脑操作，号称价格约为 GPT-5.6 的三分之一、速度三倍以上，HN 上在对比它和 Anthropic、开源模型。",["X","Hacker News"],[("X","GPT-6.1"),("Hacker News","GPT-6.1")]),
("OpenAI 宣称数学、计算机、物理三项新发现","其中一篇预印本声称推翻指数时间假设（ETH），材料已公开，尚待同行验证。",["X","Hacker News"],[("X","三项突破"),("Hacker News","三项新发现")]),
("LPL 一号种子 AL 止步 16 强","S16 瑞士轮低分淘汰赛 AL 0:2 TLAW 出局，LPL 连续两年一号种子止步 16 强。",["微博","知乎"],[("微博","LPL连续"),("知乎","AL 0:2")]),
],
"10-26":[
("卢拉赢得巴西大选连任","卢拉在第二轮击败弗拉维奥·博索纳罗，赢得第四个总统任期。",["微博","X"],[("微博","卢拉"),("X","卢拉")]),
("武契奇承认败选","塞尔维亚学生运动推动的名单在议会选举中胜出，长期执政的武契奇认输。",["微博","X"],[("微博","武契奇"),("X","武契奇")]),
("S16 瑞士轮：iG、TES 双双晋级 2-1 组","iG 击败 HLE、TES 击败 G2，两支 LPL 队伍同进 2-1 组。",["微博","知乎"],[("微博","iG 与 TES"),("知乎","HLE 0-1 iG"),("知乎","G2 0:1 TES")]),
("姆巴佩绝杀，皇马终结巴萨连胜","国家德比 2 比 1，姆巴佩打进关键球。",["微博","知乎"],[("微博","姆巴佩"),("知乎","皇马 2-1")]),
],
"10-25":[
("S16 世界赛：LPL 外战拿到首胜，TES 内战获胜","iG 拿下 LPL 在 S16 对外战的首胜，DK 翻盘 T1，LPL 队伍之间 TES 1:0 AL。",["微博","知乎"],[("微博","iG 拿下"),("微博","DK 世界赛"),("知乎","TES 1:0 AL")]),
],
"10-24":[
("谷歌芬兰数据中心砍林引狼进村","据称未做环评，当局已叫停两处工地。X 与 Reddit 同时在讨论。",["X","Reddit"],[("X","谷歌芬兰")]),
("诺基亚和 ICEYE 帮乌克兰建自主卫星网","Starlink 限速之后，乌克兰转向自建低轨通信卫星。X 与 Reddit 同时在讨论。",["X","Reddit"],[("X","诺基亚")]),
("爱泼斯坦档案风波再起","白宫被指叫停调查，Ted Lieu 引用档案内容引发争吵。X 与 Reddit 同时在讨论。",["X","Reddit"],[("X","爱泼斯坦")]),
("LPL 四队 S16 瑞士轮首轮全败","iG、TES、BLG、AL 首轮全输。知乎与微博同题。",["知乎","微博"],[("知乎","LPL 四队")]),
("泽连斯基愿拿领土换和平，俄方同意恢复三方谈判","知乎与 X 同题；俄方说 11 月中旬恢复谈判。",["知乎","X"],[("知乎","泽连斯基")]),
]}
# ---------- 10/28 (X + HN only; other platforms missing) ----------
import os as _os
def _load(day):
    inbox="/workspace/digest-inbox"
    p={}
    fx=f"{inbox}/X-2026-{day}.json"
    if _os.path.exists(fx):
        j=json.load(open(fx,encoding="utf-8"))
        p["X"]={"note":"北京时间 "+day.replace("-","月",1)+"日","items":[I(it["title"],it.get("summary",""),[("X 新闻",it["url"])],bool(it.get("cross_platform"))) for it in j["items"]]}
    fh=f"{inbox}/hackernews-2026-{day}.json"
    if _os.path.exists(fh):
        j=json.load(open(fh,encoding="utf-8"))
        p["Hacker News"]={"note":"过去 24 小时按分数排序","items":[I(it["标题"],it.get("说明",""),[("原文链接",it["原文链接"]),("HN 讨论",it["HN讨论链接"])],bool(it.get("🔥")),heat="▲"+str(it.get("分数",""))) for it in j["条目"]]}
    return p
D["10-28"]={"label":"10月28日 周三","p":_load("10-28")}
CROSS.setdefault("10-28",[])
# ---------- 10/29 (all five platforms) ----------
def _load29():
    inbox="/workspace/digest-inbox"; day="2026-10-29"; p={}
    HOT={"微博":["苹果发布会","iG时隔","西班牙列车","姆巴佩"],"知乎":["iG 2:1","西班牙高铁","姆巴佩"],"X":["eMudhra"],"Hacker News":["eMudhra","MacBook Pro"]}
    def hot(pl,t): return any(k in t for k in HOT.get(pl,[]))
    j=json.load(open(f"{inbox}/微博-{day}.json",encoding="utf-8"))
    p["微博"]={"note":"2026-10-29 09:05；🔥 为与其他平台同题","items":[I(it["title"],it.get("summary",""),[("微博热搜",it["url"])],hot("微博",it["title"])) for it in j["items"]]}
    j=json.load(open(f"{inbox}/X-{day}.json",encoding="utf-8"))
    p["X"]={"note":"北京时间 10 月 29 日；🔥 为与 HN 同题","items":[I(it["title"],it.get("summary",""),[("X 新闻",it["url"])],hot("X",it["title"])) for it in j["items"]]}
    j=json.load(open(f"{inbox}/xiaohongshu-{day}.json",encoding="utf-8"))
    p["小红书"]={"note":"小红书热榜（60s API）；榜单与前几天一致","items":[I(it["title"],it.get("desc","").replace("（与昨日一致）",""),[("搜索",it["link"])],heat=it.get("heat","").replace("w","万")) for it in j]}
    j=json.load(open(f"{inbox}/hackernews-{day}.json",encoding="utf-8"))
    p["Hacker News"]={"note":"过去 24 小时按分数排序；🔥 为与 X、微博同题","items":[I(it["title_zh"],it.get("summary",""),[("原文链接",it["url"]),("HN 讨论",it["hn_url"])],hot("Hacker News",it["title_zh"]),heat="▲"+str(it.get("points",""))) for it in j["items"]]}
    j=json.load(open(f"{inbox}/zhihu-{day}.json",encoding="utf-8"))
    p["知乎"]={"note":"知乎热榜；🔥 为与微博同题","items":[I(it["title"],it.get("summary",""),[("知乎",it["url"])],hot("知乎",it["title"])) for it in j["items"]]}
    return p
D["10-29"]={"label":"10月29日 周四","p":_load29()}
CROSS["10-29"]=[
("iG 时隔 2565 天重返 S16 淘汰赛","iG 2:1 击败 LYON 晋级八强，成为本届首支进淘汰赛的 LPL 队伍，TheShy 表现成焦点。",["微博","知乎"],[("微博","iG时隔"),("知乎","iG 2:1")]),
("西班牙高铁相撞已致 68 人死亡","托莱多附近两列高铁相撞，有中国公民受伤，初步调查指向人为失误。",["微博","知乎"],[("微博","西班牙列车"),("知乎","西班牙高铁")]),
("苹果发布首款触屏 MacBook Pro","PROLED XDR 双层 OLED 屏、M5 Pro/Max，国行 22999 元起，10 月 30 日预购；HN 上为 Mac 加触屏吵翻了。",["微博","Hacker News"],[("微博","苹果发布会"),("Hacker News","MacBook Pro")]),
("macOS 的 git 仍信任已泄露的 eMudhra 证书","Safari 已封禁，但 macOS 27.2 没覆盖 git 等命令行工具，存在中间人风险，HN 分数破千。",["X","Hacker News"],[("X","eMudhra"),("Hacker News","eMudhra")]),
("姆巴佩涉华言论事件后续","姆巴佩已道歉、外交部回应「重视当事人道歉」，微博另传其恐面临巨额赔偿。",["微博","知乎"],[("微博","姆巴佩"),("知乎","姆巴佩")]),
]
def resolve():
    out={}
    for day,lst in CROSS.items():
        out[day]=[]
        for t,d,pl,refs in lst:
            links=[]
            for pn,sub in refs:
                for k,p in D[day]["p"].items():
                    if k.startswith(pn):
                        for it in p["items"]:
                            if sub in it["t"]:
                                for lb,u in it["l"]: links.append((pn+"·"+lb,u))
                                break
            out[day].append({"t":t,"d":d,"p":pl,"l":links})
    return out
days=sorted(D.keys(),reverse=True)
for k,v in resolve().items(): D[k]['cross']=v
data=json.dumps({"order":days,"days":D},ensure_ascii=False)
html=open("template.html",encoding="utf-8").read().replace("__DATA__",data)
open("index.html","w",encoding="utf-8").write(html)
print(len(html))
