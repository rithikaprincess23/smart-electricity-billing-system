from flask import Flask, render_template, request, redirect

app = Flask(__name__)


# ==========================
# CONSUMER DATA
# ==========================

consumers = [

{
"consumer_no":"0902457831",
"name":"V Ramesh",
"door_no":"14/2",
"address":"Anna Nagar",
"area":"Sivakasi",
"meter_no":"MSK742815",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0902674198",
"name":"S Priya",
"door_no":"8/17",
"address":"Gandhi Road",
"area":"Sivakasi",
"meter_no":"MSK583924",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0902895364",
"name":"K Arun Kumar",
"door_no":"22/4",
"address":"Kamarajar Street",
"area":"Sivakasi",
"meter_no":"MSK916372",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0903125478",
"name":"P Meena",
"door_no":"5/28",
"address":"Sithurajapuram",
"area":"Sivakasi",
"meter_no":"MSK438621",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0903346189",
"name":"R Saravanan",
"door_no":"11/6",
"address":"Viswanatham Road",
"area":"Sivakasi",
"meter_no":"MSK857214",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0903567294",
"name":"M Senthil",
"door_no":"3/14",
"address":"PSV Colony",
"area":"Sivakasi",
"meter_no":"MSK941526",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0903786415",
"name":"T Nirmala",
"door_no":"27/3",
"address":"Bharathi Nagar",
"area":"Sivakasi",
"meter_no":"MSK376182",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0903948256",
"name":"G Kannan",
"door_no":"12/15",
"address":"Lakshmi Nagar",
"area":"Sivakasi",
"meter_no":"MSK824731",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0904165378",
"name":"N Mahalakshmi",
"door_no":"20/7",
"address":"Pudur",
"area":"Sivakasi",
"meter_no":"MSK532648",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0904386197",
"name":"J Murugan",
"door_no":"6/19",
"address":"AKP Nagar",
"area":"Sivakasi",
"meter_no":"MSK187354",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0904527386",
"name":"H Vijayalakshmi",
"door_no":"24/10",
"address":"Coronation Colony",
"area":"Sivakasi",
"meter_no":"MSK648219",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0904758291",
"name":"C Prakash",
"door_no":"15/8",
"address":"Muthuramalingapuram",
"area":"Sivakasi",
"meter_no":"MSK953742",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0904862147",
"name":"A Revathi",
"door_no":"16/9",
"address":"Parasakthi Colony",
"area":"Sivakasi",
"meter_no":"MSK615834",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0905173829",
"name":"D Balaji",
"door_no":"9/5",
"address":"Reserve Line",
"area":"Sivakasi",
"meter_no":"MSK792546",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0905487296",
"name":"L Kavitha",
"door_no":"18/11",
"address":"Thiruthangal Road",
"area":"Sivakasi",
"meter_no":"MSK264891",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0905793148",
"name":"S Karthik",
"door_no":"13/7",
"address":"Gnanagiri Road",
"area":"Sivakasi",
"meter_no":"MSK481926",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0906138275",
"name":"P Divya",
"door_no":"19/4",
"address":"Ramasamy Nagar",
"area":"Sivakasi",
"meter_no":"MSK573826",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0906475319",
"name":"R Dinesh",
"door_no":"10/8",
"address":"Satchiyapuram Road",
"area":"Sivakasi",
"meter_no":"MSK812473",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0906819452",
"name":"K Rekha",
"door_no":"25/6",
"address":"South Car Street",
"area":"Sivakasi",
"meter_no":"MSK394716",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0907126384",
"name":"M Senthil Kumar",
"door_no":"7/15",
"address":"Thangam Nagar",
"area":"Sivakasi",
"meter_no":"MSK614278",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0907452196",
"name":"V Malathi",
"door_no":"14/12",
"address":"Periyar Colony",
"area":"Sivakasi",
"meter_no":"MSK728415",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0907784365",
"name":"T Arunkumar",
"door_no":"8/5",
"address":"Gokulam Colony",
"area":"Sivakasi",
"meter_no":"MSK381254",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0908035729",
"name":"D Kalaivani",
"door_no":"29/2",
"address":"Eswaran Colony",
"area":"Sivakasi",
"meter_no":"MSK854236",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0908361947",
"name":"J Sathish",
"door_no":"11/27",
"address":"Sivan Kovil Street",
"area":"Sivakasi",
"meter_no":"MSK243875",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0908697253",
"name":"A Ramya",
"door_no":"17/13",
"address":"Church Street",
"area":"Sivakasi",
"meter_no":"MSK618495",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0908924618",
"name":"C Mohanraj",
"door_no":"4/9",
"address":"New Colony",
"area":"Sivakasi",
"meter_no":"MSK194526",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0909145736",
"name":"G Devi",
"door_no":"26/20",
"address":"Raja Nagar",
"area":"Sivakasi",
"meter_no":"MSK732861",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0909276845",
"name":"H Pradeep",
"door_no":"9/24",
"address":"Gopalapuram",
"area":"Sivakasi",
"meter_no":"MSK561294",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0909387152",
"name":"R Karthikeyan",
"door_no":"8/13",
"address":"Perumal Kovil Street",
"area":"Sivakasi",
"meter_no":"MSK593821",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0909498263",
"name":"P Sangeetha",
"door_no":"17/6",
"address":"Mela Theru",
"area":"Sivakasi",
"meter_no":"MSK874615",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0909514378",
"name":"S Gokul",
"door_no":"24/9",
"address":"Keela Theru",
"area":"Sivakasi",
"meter_no":"MSK315287",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0909625481",
"name":"V Dharani",
"door_no":"11/18",
"address":"Vinayagar Street",
"area":"Sivakasi",
"meter_no":"MSK728419",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0909736594",
"name":"M Arun Prasad",
"door_no":"5/27",
"address":"Balaji Nagar",
"area":"Sivakasi",
"meter_no":"MSK461852",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0909847615",
"name":"K Lavanya",
"door_no":"19/11",
"address":"Thiruvalluvar Nagar",
"area":"Sivakasi",
"meter_no":"MSK954126",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0909958726",
"name":"J Suresh Babu",
"door_no":"7/19",
"address":"Teachers Nagar",
"area":"Sivakasi",
"meter_no":"MSK246875",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0910163847",
"name":"A Poornima",
"door_no":"15/22",
"address":"Thendral Colony",
"area":"Sivakasi",
"meter_no":"MSK681943",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0910274958",
"name":"N Dinesh Kumar",
"door_no":"22/8",
"address":"Ambedkar Nagar",
"area":"Sivakasi",
"meter_no":"MSK354728",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0910385169",
"name":"C Rajeswari",
"door_no":"13/16",
"address":"Raja Colony",
"area":"Sivakasi",
"meter_no":"MSK817234",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0910496273",
"name":"T Kannan",
"door_no":"9/3",
"address":"Sri Nagar",
"area":"Sivakasi",
"meter_no":"MSK529486",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0910517384",
"name":"H Meenakshi",
"door_no":"26/14",
"address":"Gandhi Colony",
"area":"Sivakasi",
"meter_no":"MSK742591",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0910628495",
"name":"L Prabhakaran",
"door_no":"4/20",
"address":"Shanthi Colony",
"area":"Sivakasi",
"meter_no":"MSK285614",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0910739516",
"name":"R Swathi",
"door_no":"18/7",
"address":"Rajaji Nagar",
"area":"Sivakasi",
"meter_no":"MSK913548",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0910842637",
"name":"P Vignesh",
"door_no":"30/5",
"address":"VOC Colony",
"area":"Sivakasi",
"meter_no":"MSK637251",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0910953748",
"name":"S Nivetha",
"door_no":"12/9",
"address":"Kamarajapuram",
"area":"Sivakasi",
"meter_no":"MSK482736",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0911064859",
"name":"M Kannan",
"door_no":"21/15",
"address":"Lakshmi Colony",
"area":"Sivakasi",
"meter_no":"MSK759284",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0911175962",
"name":"V Revathi",
"door_no":"6/18",
"address":"Sakthi Nagar",
"area":"Sivakasi",
"meter_no":"MSK316845",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0911286073",
"name":"R Balaji",
"door_no":"16/4",
"address":"Kurinji Nagar",
"area":"Sivakasi",
"meter_no":"MSK864219",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0911397184",
"name":"K Suresh",
"door_no":"23/7",
"address":"Muthu Nagar",
"area":"Sivakasi",
"meter_no":"MSK527394",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0911408295",
"name":"P Kavitha",
"door_no":"10/16",
"address":"Vasantham Nagar",
"area":"Sivakasi",
"meter_no":"MSK681735",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0911519368",
"name":"D Praveen",
"door_no":"14/21",
"address":"Bharathi Nagar",
"area":"Sivakasi",
"meter_no":"MSK294861",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0911620479",
"name":"A Meena",
"door_no":"27/8",
"address":"Anbu Nagar",
"area":"Sivakasi",
"meter_no":"MSK738425",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0911731586",
"name":"G Vimal",
"door_no":"8/14",
"address":"Vivekananda Street",
"area":"Sivakasi",
"meter_no":"MSK415829",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0911842697",
"name":"S Priyadharshini",
"door_no":"19/5",
"address":"Nehru Colony",
"area":"Sivakasi",
"meter_no":"MSK826413",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0911953708",
"name":"R Mohan",
"door_no":"25/12",
"address":"Amman Nagar",
"area":"Sivakasi",
"meter_no":"MSK359724",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0912064819",
"name":"T Nandhini",
"door_no":"13/20",
"address":"Kamarajar Street",
"area":"Sivakasi",
"meter_no":"MSK947261",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0912175924",
"name":"V Saravanan",
"door_no":"7/26",
"address":"Sithurajapuram",
"area":"Sivakasi",
"meter_no":"MSK538472",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0912286035",
"name":"M Deepika",
"door_no":"18/9",
"address":"Viswanatham Road",
"area":"Sivakasi",
"meter_no":"MSK761928",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0912397146",
"name":"P Aravind",
"door_no":"4/11",
"address":"Reserve Line",
"area":"Sivakasi",
"meter_no":"MSK284639",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0912408257",
"name":"K Shanthi",
"door_no":"21/6",
"address":"Thiruthangal Road",
"area":"Sivakasi",
"meter_no":"MSK895314",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0912519368",
"name":"R Vijay",
"door_no":"15/23",
"address":"Parasakthi Colony",
"area":"Sivakasi",
"meter_no":"MSK426781",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0912620473",
"name":"A Lakshmi",
"door_no":"9/17",
"address":"Gnanagiri Road",
"area":"Sivakasi",
"meter_no":"MSK738596",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0912731584",
"name":"S Kumar",
"door_no":"12/7",
"address":"Anna Nagar Extension",
"area":"Sivakasi",
"meter_no":"MSK614937",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0912842695",
"name":"N Revathi",
"door_no":"20/14",
"address":"Gandhi Road Extension",
"area":"Sivakasi",
"meter_no":"MSK825146",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0912953706",
"name":"B Karthik",
"door_no":"6/24",
"address":"MGR Nagar",
"area":"Sivakasi",
"meter_no":"MSK397528",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0913064817",
"name":"P Uma",
"door_no":"16/12",
"address":"Raja Nagar",
"area":"Sivakasi",
"meter_no":"MSK748315",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0913175928",
"name":"J Naveen",
"door_no":"28/5",
"address":"VOC Nagar",
"area":"Sivakasi",
"meter_no":"MSK536824",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0913286039",
"name":"C Priya",
"door_no":"11/19",
"address":"Housing Board",
"area":"Sivakasi",
"meter_no":"MSK912457",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0913397140",
"name":"H Ramesh",
"door_no":"3/16",
"address":"Old Bus Stand Road",
"area":"Sivakasi",
"meter_no":"MSK684291",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0913408251",
"name":"L Sangeetha",
"door_no":"17/9",
"address":"Sakthi Nagar",
"area":"Sivakasi",
"meter_no":"MSK475829",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0913519362",
"name":"D Murugan",
"door_no":"24/15",
"address":"Kovilpatti Road",
"area":"Sivakasi",
"meter_no":"MSK836214",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0913620473",
"name":"V Kannan",
"door_no":"8/20",
"address":"Lakshmi Nagar",
"area":"Sivakasi",
"meter_no":"MSK291745",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0913731584",
"name":"R Priya",
"door_no":"13/6",
"address":"Thendral Nagar",
"area":"Sivakasi",
"meter_no":"MSK647382",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0913842695",
"name":"M Sathish",
"door_no":"22/11",
"address":"Nehru Road",
"area":"Sivakasi",
"meter_no":"MSK518936",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0913953706",
"name":"A Revathi",
"door_no":"5/18",
"address":"Teachers Colony",
"area":"Sivakasi",
"meter_no":"MSK729451",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0914064817",
"name":"P Dinesh",
"door_no":"19/3",
"address":"New Colony",
"area":"Sivakasi",
"meter_no":"MSK364827",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0914175928",
"name":"S Karthika",
"door_no":"10/21",
"address":"Muthuramalingapuram",
"area":"Sivakasi",
"meter_no":"MSK852741",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0914286039",
"name":"G Balaji",
"door_no":"26/8",
"address":"RTO Road",
"area":"Sivakasi",
"meter_no":"MSK473926",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0914397140",
"name":"N Mahesh",
"door_no":"14/5",
"address":"Krishnapuram",
"area":"Sivakasi",
"meter_no":"MSK618247",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0914408251",
"name":"V Kavitha",
"door_no":"23/10",
"address":"AKP Nagar",
"area":"Sivakasi",
"meter_no":"MSK934715",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0914519362",
"name":"J Prakash",
"door_no":"6/13",
"address":"Pudur",
"area":"Sivakasi",
"meter_no":"MSK275849",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0914620473",
"name":"T Nirmala",
"door_no":"18/24",
"address":"Coronation Colony",
"area":"Sivakasi",
"meter_no":"MSK746382",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0914731584",
"name":"R Mohan",
"door_no":"9/16",
"address":"Sivan Kovil Street",
"area":"Sivakasi",
"meter_no":"MSK381625",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0914842695",
"name":"P Suresh",
"door_no":"12/25",
"address":"Viswanatham Road Extension",
"area":"Sivakasi",
"meter_no":"MSK529741",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0914953706",
"name":"K Divya",
"door_no":"20/9",
"address":"Gandhi Nagar",
"area":"Sivakasi",
"meter_no":"MSK816394",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0915064817",
"name":"M Aravind",
"door_no":"7/14",
"address":"Kamarajar Nagar",
"area":"Sivakasi",
"meter_no":"MSK437825",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0915175928",
"name":"A Selvi",
"door_no":"25/17",
"address":"Bharathi Nagar Extension",
"area":"Sivakasi",
"meter_no":"MSK694218",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0915286039",
"name":"R Vijayakumar",
"door_no":"15/6",
"address":"Reserve Line Extension",
"area":"Sivakasi",
"meter_no":"MSK285739",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0915397140",
"name":"L Nandhini",
"door_no":"4/22",
"address":"Sakthi Colony",
"area":"Sivakasi",
"meter_no":"MSK753926",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0915408251",
"name":"S Balaji",
"door_no":"28/11",
"address":"Anna Nagar South",
"area":"Sivakasi",
"meter_no":"MSK418562",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0915519362",
"name":"C Lakshmi",
"door_no":"11/8",
"address":"Gnanagiri Road Extension",
"area":"Sivakasi",
"meter_no":"MSK629473",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0915620473",
"name":"H Praveen",
"door_no":"21/14",
"address":"Thiruthangal Road Extension",
"area":"Sivakasi",
"meter_no":"MSK384916",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0915731584",
"name":"N Deepa",
"door_no":"8/19",
"address":"Parasakthi Nagar",
"area":"Sivakasi",
"meter_no":"MSK745281",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0915842695",
"name":"G Senthil",
"door_no":"16/7",
"address":"MGR Nagar Extension",
"area":"Sivakasi",
"meter_no":"MSK216938",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0915953706",
"name":"V Uma",
"door_no":"29/12",
"address":"Housing Board Extension",
"area":"Sivakasi",
"meter_no":"MSK857624",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0916064817",
"name":"P Karthik",
"door_no":"13/21",
"address":"VOC Nagar Extension",
"area":"Sivakasi",
"meter_no":"MSK492715",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0916175928",
"name":"S Revathi",
"door_no":"5/15",
"address":"Raja Nagar Extension",
"area":"Sivakasi",
"meter_no":"MSK738462",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0916286039",
"name":"D Ramesh",
"door_no":"18/4",
"address":"Kasi Viswanatham Nagar",
"area":"Sivakasi",
"meter_no":"MSK561824",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0916397140",
"name":"A Priya",
"door_no":"24/16",
"address":"Vinayagar Colony Extension",
"area":"Sivakasi",
"meter_no":"MSK824639",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0916408251",
"name":"M Kumar",
"door_no":"9/13",
"address":"Old Market Road",
"area":"Sivakasi",
"meter_no":"MSK375918",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0916519362",
"name":"K Revathi",
"door_no":"15/20",
"address":"Amman Kovil Street Extension",
"area":"Sivakasi",
"meter_no":"MSK946275",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0916620473",
"name":"J Siva",
"door_no":"6/8",
"address":"Nehru Nagar",
"area":"Sivakasi",
"meter_no":"MSK218457",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0916731584",
"name":"P Meena",
"door_no":"27/11",
"address":"Krishna Colony",
"area":"Sivakasi",
"meter_no":"MSK735824",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0916842695",
"name":"R Prakash",
"door_no":"12/18",
"address":"Sivakasi Town Area",
"area":"Sivakasi",
"meter_no":"MSK482916",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0910238457",
"name":"R Mohan",
"door_no":"18/4",
"address":"Sri Ram Nagar",
"area":"Sivakasi",
"meter_no":"MSK834521",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0910456723",
"name":"K Revathi",
"door_no":"12/8",
"address":"K.K. Nagar",
"area":"Sivakasi",
"meter_no":"MSK572914",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0910674385",
"name":"S Prakash",
"door_no":"6/14",
"address":"VOC Street",
"area":"Sivakasi",
"meter_no":"MSK691248",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0910892156",
"name":"M Kavitha",
"door_no":"24/9",
"address":"Ayyanar Colony",
"area":"Sivakasi",
"meter_no":"MSK845372",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0911027843",
"name":"P Hari",
"door_no":"15/3",
"address":"Vinayagar Colony",
"area":"Sivakasi",
"meter_no":"MSK263845",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0911245368",
"name":"T Selvi",
"door_no":"10/17",
"address":"North Street",
"area":"Sivakasi",
"meter_no":"MSK714952",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0911462985",
"name":"A Dinesh",
"door_no":"28/6",
"address":"Mariamman Kovil Street",
"area":"Sivakasi",
"meter_no":"MSK958413",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0911687542",
"name":"V Lakshmi",
"door_no":"7/11",
"address":"Jawahar Nagar",
"area":"Sivakasi",
"meter_no":"MSK436728",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0911893476",
"name":"N Rajesh",
"door_no":"20/5",
"address":"Nehru Road",
"area":"Sivakasi",
"meter_no":"MSK825194",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0912056834",
"name":"G Meenakshi",
"door_no":"9/13",
"address":"Teachers Colony",
"area":"Sivakasi",
"meter_no":"MSK347862",
"category":"House",
"status":"Active"
},

{
"consumer_no":"0916953718",
"name":"Sri Lakshmi Traders",
"door_no":"12/5",
"address":"Gandhi Road",
"area":"Sivakasi",
"meter_no":"MSK812945",
"category":"Office",
"status":"Active"
},

{
"consumer_no":"0917064829",
"name":"Vijaya Finance Office",
"door_no":"8/14",
"address":"Kamarajar Street",
"area":"Sivakasi",
"meter_no":"MSK473826",
"category":"Office",
"status":"Active"
},

{
"consumer_no":"0917175930",
"name":"Siva Accounts Office",
"door_no":"21/3",
"address":"Thiruthangal Road",
"area":"Sivakasi",
"meter_no":"MSK695218",
"category":"Office",
"status":"Active"
},

{
"consumer_no":"0917286041",
"name":"Tamil Solutions",
"door_no":"15/9",
"address":"Viswanatham Road",
"area":"Sivakasi",
"meter_no":"MSK384761",
"category":"Office",
"status":"Active"
},

{
"consumer_no":"0917397152",
"name":"Kavin Enterprises",
"door_no":"6/20",
"address":"Reserve Line",
"area":"Sivakasi",
"meter_no":"MSK927435",
"category":"Office",
"status":"Active"
},

{
"consumer_no":"0917408263",
"name":"Raja Consultancy",
"door_no":"18/6",
"address":"Anna Nagar",
"area":"Sivakasi",
"meter_no":"MSK546829",
"category":"Office",
"status":"Active"
},

{
"consumer_no":"0917519374",
"name":"Green Tech Office",
"door_no":"24/11",
"address":"Bharathi Nagar",
"area":"Sivakasi",
"meter_no":"MSK738415",
"category":"Office",
"status":"Active"
},

{
"consumer_no":"0917620485",
"name":"Sri Balaji Agency",
"door_no":"10/16",
"address":"New Bus Stand Road",
"area":"Sivakasi",
"meter_no":"MSK294876",
"category":"Office",
"status":"Active"
},

{
"consumer_no":"0917731596",
"name":"Arun Business Centre",
"door_no":"5/22",
"address":"Gnanagiri Road",
"area":"Sivakasi",
"meter_no":"MSK861437",
"category":"Office",
"status":"Active"
},

{
"consumer_no":"0917842607",
"name":"Vasanth Office Solutions",
"door_no":"19/8",
"address":"Kasi Viswanatham Street",
"area":"Sivakasi",
"meter_no":"MSK625394",
"category":"Office",
"status":"Active"
},

{
"consumer_no":"0917953718",
"name":"Sri Vinayaga Fireworks Factory",
"door_no":"3/25",
"address":"Sithurajapuram Outer Area",
"area":"Sivakasi",
"meter_no":"MSK918452",
"category":"Factory",
"status":"Active"
},

{
"consumer_no":"0918064829",
"name":"Anbu Match Works",
"door_no":"7/18",
"address":"Kalayarkurichi Road",
"area":"Sivakasi",
"meter_no":"MSK562839",
"category":"Factory",
"status":"Active"
},

{
"consumer_no":"0918175930",
"name":"Sri Murugan Crackers Unit",
"door_no":"12/9",
"address":"Kariapatti Road",
"area":"Sivakasi",
"meter_no":"MSK734826",
"category":"Factory",
"status":"Active"
},

{
"consumer_no":"0918286041",
"name":"Lakshmi Pyrotechnics",
"door_no":"5/14",
"address":"Virudhunagar Road Outer",
"area":"Sivakasi",
"meter_no":"MSK485917",
"category":"Factory",
"status":"Active"
},

{
"consumer_no":"0918397152",
"name":"Vijaya Match Industries",
"door_no":"18/6",
"address":"Thiruthangal Outer Area",
"area":"Sivakasi",
"meter_no":"MSK826394",
"category":"Factory",
"status":"Active"
},

{
"consumer_no":"0918408263",
"name":"Sakthi Fireworks Industries",
"door_no":"22/4",
"address":"Sattur Road Outer Area",
"area":"Sivakasi",
"meter_no":"MSK647392",
"category":"Factory",
"status":"Active"
},

{
"consumer_no":"0918519374",
"name":"Kannan Match Factory",
"door_no":"9/12",
"address":"Mettamalai Road",
"area":"Sivakasi",
"meter_no":"MSK293847",
"category":"Factory",
"status":"Active"
},

{
"consumer_no":"0918620485",
"name":"Raja Paper Products",
"door_no":"15/8",
"address":"Kovilpatti Road Outer",
"area":"Sivakasi",
"meter_no":"MSK758214",
"category":"Factory",
"status":"Active"
},

{
"consumer_no":"0918731596",
"name":"Sri Balaji Explosives Unit",
"door_no":"6/17",
"address":"Alangulam Road",
"area":"Sivakasi",
"meter_no":"MSK419583",
"category":"Factory",
"status":"Active"
},

{
"consumer_no":"0918842607",
"name":"Vasantha Industries",
"door_no":"25/3",
"address":"Aruppukottai Road Outer",
"area":"Sivakasi",
"meter_no":"MSK836925",
"category":"Factory",
"status":"Active"
}

]# ==========================
# HOME
# ==========================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# LOGIN PAGES
# ==========================

@app.route("/admin-login")
def admin_login():
    return render_template("admin-login.html")


@app.route("/consumer-login")
def consumer_login():
    return render_template("consumer-login.html")


@app.route("/meter-reader-login")
def meter_reader_login():
    return render_template("meter-reader-login.html")



# ==========================
# ADMIN DASHBOARD
# ==========================

@app.route("/admin-dashboard")
def admin_dashboard():
    return render_template("admin-dashboard.html")


@app.route("/dashboard-home")
def dashboard_home():
    return render_template("dashboard-home.html")



# ==========================
# ADD CONSUMER SAVE
# ==========================

@app.route("/add-consumer", methods=["GET","POST"])
def add_consumer():

    if request.method == "POST":

        new_consumer = {

            "consumer_no": request.form["consumer_no"],
            "name": request.form["name"],
            "door_no": request.form["door_no"],
            "address": request.form["address"],
            "area": request.form["city"],
            "meter_no": request.form["meter_no"],
            "category": request.form["category"],
            "status": request.form["status"]

        }

        consumers.append(new_consumer)

        return redirect("/view-consumer")


    return render_template("add-consumer.html")



# ==========================
# VIEW CONSUMER
# ==========================

@app.route("/view-consumer")
def view_consumer():

    return render_template(
        "view-consumer.html",
        consumers=consumers
    )



# ==========================
# CATEGORY
# ==========================

@app.route("/house")
def house():

    house_data = []

    for c in consumers:
        if c["category"] == "House":
            house_data.append(c)

    return render_template(
        "house.html",
        consumers=house_data
    ) 

@app.route("/office")
def office():

    office_data = []

    for c in consumers:
        if c["category"] == "Office":
            office_data.append(c)

    return render_template(
        "office.html",
        consumers=office_data
    )



@app.route("/factory")
def factory():

    factory_data = []

    for c in consumers:
        if c["category"] == "Factory":
            factory_data.append(c)

    return render_template(
        "factory.html",
        consumers=factory_data
    )

# ==========================
# METER READER
# ==========================

@app.route("/meter-reader")
def meter_reader():
    return render_template("meter-reader.html")

@app.route("/meter-reader-dashboard")
def meter_reader_dashboard():
    return render_template("meter-reader-dashboard.html")


@app.route("/meter-reading")
def meter_reading():
    return render_template("meter-reading.html")



# ==========================
# BILL & PAYMENT
# ==========================

@app.route("/bill-calculation")
def bill_calculation():
    return render_template("bill-calculation.html")


@app.route("/payment")
def payment():
    return render_template("payment.html")


@app.route("/reports")
def reports():
    return render_template("reports.html")



# ==========================
# CONSUMER DASHBOARD
# ==========================

@app.route("/consumer-dashboard")
def consumer_dashboard():
    return render_template("consumer-dashboard.html")


@app.route("/bill-receipt")
def bill_receipt():
    return render_template("bill-receipt.html")

@app.route("/payment-success")
def payment_success():
    return render_template("payment-success.html")

# ==========================
# RUN APP
# ==========================

if __name__ == "__main__":
    app.run(debug=True)