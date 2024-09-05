""" chall.py

from out import enc, R
from math import prod

flag = ''
a = [0]
for i in range(355):
    b = [_+1 for _ in a]
    c = [_+1 for _ in b]
    a += b + c

    print(a)
    input()
    if i%5 == 0:
        flag += chr(enc[i//5] ^ prod([a[_] for _ in R[i//5]]))
        print(flag)
"""

""" out.py

enc = [65, 331, 1783, 6186, 6470, 17283, 25622, 49328, 75517, 80689, 148293, 164737, 256906, 285586, 529890, 453524, 486833, 612780, 995834, 1034513, 1164566, 1187257, 1195463, 1481795, 1456512, 2255447, 1918038, 2402807, 3279260, 2958036, 2881150, 3263588, 3820625, 4237730, 5185459, 5233235, 6049254, 6786968, 6183125, 8612625, 8897839, 8945969, 8548390, 9936098, 9754219, 10421226, 12312594, 13139249, 13528562, 13806877, 14378265, 14232673, 17206117, 17924517, 19586568, 21397250, 22214087, 25159893, 25280690, 27657640, 29296934, 29729604, 28262064, 32050040, 32629604, 33546289, 38222149, 38457097, 34401800, 39471481, 41751527]
R = [[1, 1, 2], [573, 229, 206], [10885, 41497, 160304], [8839119, 14295644, 29685237], [10280936393, 8467023078, 4707689596], [945960776097, 1031182232283, 69972907378], [137665703218004, 35525403452985, 138350929229224], [122336169683982108, 59224551586149213, 118549674466202725], [13626900512752906569, 3897136862695780183, 35076404995397046345], [163593922657921448706, 2585968319357630198594, 6996211172572711470196], [1433471461923638870900801, 327749274075770619032029, 392888374649818189286143], [19744782485775287314957049, 460634978666194064781998391, 31659469833364582430102473], [6307006601660265171992374053, 98623451654268880809155078560, 64233892285570757739641890442], [29154577259006185142961063158052, 9914420641115443182131036644284, 7279481296300468961689254189816], [1558076296273259698341440069238056, 4310691260512125134140007179935352, 4980109395532057935132560488460615], [1405212213206399714548754108042831062, 147404700816591482365933597995505421, 1687342229905046884455484428290534831], [178231026292428921004703562165525411894, 412963066680488665482944489625497608212, 70340936836695689283893473181751382743], [56698349585950537262338505181144336979587, 52217406711284315435595033610018391654195, 62108893391408870656968514251159189194521], [23893381410382084563262913681592457710903753, 22212431596810321024205206524427117951881276, 19989366146226118433589584982546380299442529], [2889511959527885324209305298200285677701094725, 2606035783027360737177505608659564857175468342, 912571494124990709836860172316232544276438933], [1228504793022169504797984188122406171358072857562, 1363360236293969893605831020276765744813251042404, 297563475302044806097863947023814157856389926467], [175608219147292209879121072264875458914106479644056, 315961037093380016583816358395509380577071641993080, 239337133002097856335802829217431187967280790555618], [86907177537979343798282102958682278554281933300161219, 64317934619982444261646548589166853140812442454915939, 88018844277704099677399755876858185474535387410720445], [7578403250388931197644961338635760720785818764109837460, 3274632430417597288151262115132742324278216710102859849, 21631882539927419463654991077819010737499996516834371896], [1784005907786440158922591109117656913793076162623216189690, 584544132694337139275683959718819628005872667061541957378, 468567183178097211759022580480616535344925394592430209347], [729938520575815549919101929342052441361022063727469070145908, 274550060366659698888268478648666070589265337265466015158929, 816678505785021313430715270084566186204139128920927645737535], [106419295808981221951748024239581079670028738895932201279327601, 228539844398841595052385901358010923608064510380402434702609661, 273988143389250335223734499597874248431371549060210491714569562], [49610527461979411507467246924089752425201348016881391697347424513, 69137173214147289942692162771140621271832934031257876965711710949, 62730418740220882006739225333147856993853932330719923493210890436], [16851730736657444946446580883690706974734423996859949550565127900099, 17020082067082804201146138962045534353417049142267440365496556106646, 8425831360975428058545914350645398599666494245768262308563962500419], [1744457135330206658118333956018617505833961797560206981881297005844650, 2488272677039458908993320500395188112777156174503950549584903141127805, 2025261799014127885373424699982740002932128127330675129998065148842076], [911346406564292964244181957884281723110968676471292861562401898225344617, 515016108655135831997810719937894761768485489577746685305628286718842981, 529790162728531781327256209611140765345349305272432962612449845910133431], [188862868604458670709430534588424053453382627459433615665235632604774195105, 159265669796915366090971144664529549841435257409990033156402470728739515566, 60682317875971312140589380343235690226249919927211583007002668602340443573], [55193706264542603342210130740272648982338137150197933176657775220529084548357, 27195911554042477052963544743968295593780567038751440659821492286699921720191, 29560858927273910749887729332550032054935265811253142815881982028400038247319], [7967504222642156771288173955589952284643390129548188481154174503319661178503072, 1359513209197691298598578835648210368417270153147787219079370527092612752268982, 9230224122977955411941024673666600930203300543850914931726268334960580194164492], [831700796347413410615911772707996893565701575245034815476696517314277469580570895, 348270496636109272924978536225447046371768965881221748966431208037510608509018947, 1374142394998218750798266411208358766099463968207325565770298390782412190916814310], [728134218644001393441390399108789642515528723649320724369274506318570415182986524315, 742827622102241979512100045719273776927502266118292292534558855112165931221386202274, 834896424809769450256618602072325069420072099322355588900296733100469513421816291082], [66657521960797189904538245565000331457185183590890330549573802546986185313721475396700, 156009195280892389693769014846212616019395180017555815307430719390512302340174696802961, 200597453219232827796159650057256671048223063579900089130489322256618558160451930790328], [29037802387828000295889248231258384842641658132563570380131111284295279711886813738722877, 19026977082052219356279509080995574655135318523161839766669049352934239566123435130632269, 39761369983488555876764613607529231297124885693027657193256415982138011913990538842193676], [12561577796321365976754879894302013598558663721653793677134296816829605195336351648166256979, 12838267657320533157115690870383947765475624026880560207257146094964304690365021016825129853, 7495910847481301240802133743653617325920902801350946983901641264085048246865582593139729403], [3041492422855245745694700380550203206979029337703391421024168530121179356261997345191319516771, 640848136862288646629516649150957018999642176847724807173173190110594937936496769080786522049, 2969396567186077593954887271522825649221970125735131131175295619859668697895377679704620087889], [81093296695439965954342113512388849103885378349927499243812089963712022532857570393423108003659, 207270172491583465284894346681199376583340220798632240230546015429407709634891762897301883017884, 190032100106748542252716447896640624640777006597630648586475349805342010386746524668165629317161], [32533344401268273967114633758559931826617665158198522614215035245432490850547861982523840145942074, 63037110804852476247528611221542679314242047661614004564491126914186621243875589339803531182020426, 124951290010810803694525061731704200016278732642269550252996419375511248225453431694350800495944347], [35137716753067452090927097050636563619547995454738820278063768022488025199701346321134314448841872794, 12985633921598678956642044617726801111706054490973834029123104709195008027204480882797267867341064476, 5305727297771409651023243066103178878140492848258919185568928165081859031657272186995329239806104118], [3762249421419366884537098419354305781080227852906891797970952858114351664324268703722577235910347584304, 1550561491002149215075653857319603880429910437941882645815693111090526036411984733619993307966461840126, 9381201201142531265853888435902828303237464579889417263110360168656884858562872253087408205544357087306], [2056899273710648314295675026370994461871817025547273056051947505619792320735406178540815338367649803736698, 2400734502375026278495337239471134511733068748104902082380177269089395799760690047001894688755690156943965, 1732882327457919111959549262162185466220677456316057330624797413276486794416719248300528086966180252303114], [652896416106612920827629685957065255447694536466438605951176120897225559332173369105354682171886992371096271, 454656456599989954897128567415348109820116193092249211381080865675729251399216425900943035094745504751551478, 313462687528796654990235524389154265472701132978608107344549946439400139763799796696708655697709590458851693], [104545083165292290401534689701271365665130721684233823742393188465642248906869971808131422905737188031748198141, 143435659999076222337918882839514881215221734734388221592284254721485478080813955224165205293052195097128579855, 40702920019369144545229507759809584949672965917473112280581406604369595519129367208280022299388654288711154666], [38503581328033455359533847919966468672140392024444493807653196910126532016690751491942280634907485938880904383892, 18884661042488142899588244068961327261179761242819343293800084248732455991582145396596568605394801002264811582913, 9384187667567328792366639242333135973520260966794149958963790153859412473452108461030094493051859371952206600103], [1324740544139254318273253770332855107671134390702432855738006366746449029576545099512912405134518891320718185169513, 303109855383738809002288742946345379428808745080383659457773592835713207285305179350437080179436990935112214270665, 1624316398491836088831202617387140081826145335528105327252325808416312557534737052667304856958627845436851248489907], [1401688155035324575988216421089538478215416341501120197948850057036940982809195355604792139051606198616259749003767965, 2048526767570983439518103534423786218930891544461790174537795037321458400711335285803377717794909411012955744133476255, 1762727028524336180955903313027800157402368747053245589279568985101199159336178410704769284913872366668626620722820001], [50297209609059623442815521181722350352719290856519522344205021656047917502237970917310786375279675448048523557477430805, 15857002182452297197982329375111053201349508644473177012866786518888614594064540203474772864651339444396084341878515576, 403895394397791973760362815402896437377344978600840941064554187621230430084298005374238342732262063840044910975524068949], [20927895257497747238986668613021753703988641935802190249109474260700254931957028009020124444515606174885105200514424695082, 98413334887257200681733050277146006881243886515744398160788872174047591102175251363062934975915162936537446741657116020142, 78051558442599615087309433778145628490452507646127324484751553881813231026055047222156670588293781138503172604228380321976], [16192599784864691180295806644680526068139201230224367938291307055217817451931595148327785761709610349158459120162594696721314, 25611869083247087245152286117827285218210603087717473516754579003267021231851741943325038005987943686029851783456188413428074, 25992180689931116336143095391720658271235318487491891937170995569452091167110261435363933440750176011418320077925229437139441], [1486065074770625241543033346926580865585132960697717056411171079869255497066621227141079321338459582851303823888054029997147496, 3245525951376819329573085322535606750874380802419239054828998013409477579195505568845403155178550250571620183484642153687084244, 112418439871405702093723993558148045955947964355568790237500341233964777308030963124075783317247912243584957552429165175567188], [554414264583315659699674517123338050716408838397305952512626047866746893643260154358369760406409101186772630676890380049965307590, 1043200414999535582462864439522105588377941946109653277868282881800541041225127481024498906645711562172897887223370490480497681412, 1871431105609054802663860414521114349131507818555644333411481724711171594958225200659513765626347213458290656339411867664235748235], [109230492350394219294209686711480148111959062898867460819812302521395700744999727865321098736169431939787056320261942410874757468733, 10946993578608042700991075540593043447808613562525646016983180580734427427599503571629298569725315601140135266559866649733843666727, 246030677678827748651446732888780806311392020007912976339004498361198715345773486325046589103993759763143866861161592823427071675783], [101248109580616294936240676346296891730712143388596188295797877367588968569639645896673577202008557062368850136081432452565741764481780, 72117245758610730163502698117383423435096962164217931641814611037828628449683172552024006212893710709568092586830060674702530720630838, 34156236014950110786479179647875910303316921242375549800567936108514427153840347644258274879993941142366793077681295934860378594097995], [15990838065899635329967108817549304489054566867252353907331052546852811551057811982388652520412231526149334610863159737956306990396908939, 13877638546016696452612797658463979632180424075209018025216464738606223836856974888899865627240196446658442424067555529584318542068829304, 12677775392542654738129436028991703771671470731367401228424534633630663828784099080524940674805885560927768192511268731112718248394226507], [4296188317596592605354429710403045587794207218497978126733577807175844533640562786210144572543925369843724531281548656552721224871306408934, 285081536544994597260307396740776857794705257501212064846291286514459078443374031927697656139361855500907534462182310648076485673416888921, 520400706696766574333742507514386230765824087521995208501834759618645877986879790251385446075750614955038875512629839250118760269191026622], [723122593616548907044099469723004726497190485559641744410070335219249336116342743215201071639802723683990761587106342365181354592623344218801, 1153081974669760235610536228156857408078008322403018213105375405360329083793186764164405226051712297309391269434496643454473313250671026317128, 1045323654864427173281766234316255577186878737208078652772060147922139057153363756199552977634641592432020342677714487371354351937732515340769], [286030080032157831584122660246587223893513399286538292684484068916231408017197370416498756180333020768698170404223092800960480629708274198357766, 100459558673910591509973452243869469674982609364866947220110101686698490657211631881397783562822118029166972210922055667458687955478399421168073, 312292327459064171357951759470882292390813169506242332753018135455390262583056880515441693426982451446980584789275705862372219996047882719285468], [76023080448832255495664889576818310445911073068838354851978140354392238188416337217228905387684862369127475726687990437747210819206251364663178366, 79909535960128750054208617904939309393169970650206619816849976160579698275180034617070788991315683797824856913928470939644467300086993321201275631, 12836987084929344870134687159309348060974294106220115465827408756433486147899850505008319816817057038378975905890624567608788056817845202397527597], [11279020797227306692073405567334400908025941871799432354659652341662205110177284358626006856443935763650221701010232939257999415323818219101323774121, 20701716847360264680448441409193277773473820912500811296314617325114135630274188720845655325935966413579156878391231036040452436356525182168927455769, 11662490076049426720444287570232288256606203670569001212826141005750817611908212326773163654541321013641063180589777301351375281786680265675242915490], [3664976056843244899046405770495243971851225829858688853727255965918845526037369928043768545436855691031033629075777959837838040026954342398365868203284, 4303664923255399627145773380664312302061180145098884815650431155840108262865380991633139788830947418042382178669502102253270206161944686126778721177256, 1329888344611251607206799678158068345794425334107811143951615318094938592491017133110084673083835131542105919726637023746895921675774269854930747391813], [27526396919462446400199857855946211084417698150345843381184345248429342915256383060323038929143521278663384600451962926565632962402403286747322866933186, 832473066824718090282351924757867347117523355595408205531707129191210904495622372227106712804655676416188547356217198716998980216027824443061970459017213, 739285279997382078166992780609222700401048107660954429292420131543662494886151464036035917462960151020457777790199766047230392831072294938389838019192375], [241604036983256570910237563151583734634247804014729497396976621887556420166938734129084585512496813488556852332626724956813515081301022211288671489609624726, 232918625432663776612980648646547430425799068288725384437941544591137340240225694513718939585866852521983294039207611429584316281048886496760692847238475958, 330280356821375777416141788080009583520428720186288496589338440210000394525310148011506810729947920712589385371511611188538783776067961774123574958402713416], [37917177921557913063797063712175107470400149903365012052437848627624556178462092849875066084483410175131191909488280543701737678455574966120683361771538984869, 82285213220068552502977130984079405256046284613100219448045047718647214635424915048365233181766026879765932575837957606566968808956187850661636939764713829757, 54862629754020461190972199219422809877737510603527851047197196675006832975655107720818914451383313987635699626910019975156748775680769393491662354129665564665], [10176770592061494683902022210595838961181896347187166561115555380150487550055091054691083781753046719620211182526622568190117287871224755124378960411817051522347, 20391437792952018079898899709442083666375852061962519735185961685298641965953456220963572734830150545534613384697719780482366933145736561569104130664654552711112, 5184672887185762911825431869653048673959736811735614638077371148686297384863233976741655920190695071107226141719503919502011593827206165497631320711901861412505], [2773806845979032590669908316758838167490410534429658877076115296219751182626553934482865930802051989491312042105845829522334288803990327629270690684487381035735068, 4313397356511833703919769030365821724752420735506938177875096936636635640237756238703789233649487006170963871514071797499791012862391242439315785734249060209905870, 1384521522113584419234026605710886691198760220478447038149301773862983248614505122442941228842319360170622150894552550565168083692478460245750070200793173355915110], [977605605346967027884157812086795195281198128843588844802255600782574072246322450726753867594904637719389010883656117163446600576421636602802273450819657911229092739, 1077122028153411402864595787831545281960357301948562230974263019017587247307938796068349770175005165754271751912679139878240066950583364300243665524428812156594708658, 381071794273313233090141046983124159496192143355842855513220907221649906653471651139682409544512356167912597901893098050357507457603299288858937833673078904758920182], [67062212236285997924209614787534890751009288135227553165998196811919096000885310832052245686810617894345398300182072193678864438410618886008897981904472885367476211057, 159854276414635686128310856355014729303536467044176101830252797765797010129021499806804246440506719099238942904835227939207035449129236215655107335852262007504926605969, 250442077587466213725605597489854467254423721041651218597587608844522479925489283592286145881313894977088155508712509697027472708345579764134359861134589340933375529074]]
"""
from out import enc, R
from math import prod

flag = ''

# a is a long array that goes by 
# First iteration: [0, 1, 2]
# Second iteration: [0, 1, 2, 1, 2, 3, 2, 3, 4]
# It goes on...
# As you can see, the length of a is in the multiple of 3s and each "subsection" starts off from its index in the subsection increments e.g. 1, 2, 3, 4..
# This can be solved with a simple recursion function

def recur(r):
    if r // 3 == 0:
        return r % 3

    return recur(r // 3) + r % 3

for i in range(len(enc)):
    flag += chr(enc[i] ^ prod([recur(_) for _ in R[i]]))
    print(flag)

# CSCTF{2441d2f22fa1d5b9fc0a850dcfbbccf608cafbc22a1beaae0ac328ff6d218781}