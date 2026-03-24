#delimit ;
 
* Edit the import statement to reference the data file on your computer.;
 
import delimited
tucaseid
tulineno
gediv
gemetsta
gepseucl
gepseust
gereg
gestfips
gtcbsa
gtco
gtmetsta
hefaminc
hehousut
hephoneo
hetelavl
hetelhhd
hetenure
hrhhid
hrhhid2
hrhtype
hrintsta
hrlonglk
hrmis
hrmonth
hrnumhou
hrsample
hrsersuf
hryear4
hubus
hubusl1
hubusl2
hubusl3
hubusl4
hufaminc
hufinal
huhhnum
huinttyp
huprscnt
hurespli
huspnish
hxfaminc
peabspdo
peabsrsn
peafever
peafnow
peafwhen
peafwhn1
peafwhn2
peafwhn3
peafwhn4
pecert1
pecert2
pecert3
pecohab
pecyc
pedadtyp
pedipged
pedisdrs
pedisear
pediseye
pedisout
pedisphy
pedisrem
pedw4wk
pedwavl
pedwavr
pedwlko
pedwlkwk
pedwrsn
pedwwk
pedwwnto
peeduca
peern
peerncov
peernh1o
peernh2
peernhro
peernhry
peernlab
peernper
peernrt
peernuot
peernwkp
pefntvty
pegr6cor
pegrprof
pehgcomp
pehract1
pehract2
pehractt
pehravl
pehrftpt
pehrrsn1
pehrrsn2
pehrrsn3
pehrusl1
pehrusl2
pehruslt
pehrwant
pehspnon
peio1cow
peio1icd
peio1ocd
peio2cow
peio2icd
peio2ocd
pejhrsn
pejhwant
pejhwko
pelayavl
pelaydur
pelayfto
pelaylk
pelkavl
pelkdur
pelkfto
pelkll1o
pelkll2o
pelklwo
pelkm1
pelndad
pelnmom
pemaritl
pemjnum
pemjot
pemlr
pemntvty
pemomtyp
pems123
penatvty
penlfact
penlfjh
penlfret
peparent
pepdemp1
pepdemp2
peret1
perrp
peschenr
peschft
peschlvl
pesex
pespouse
prabsrea
pragna
prcitshp
prcivlf
prcow1
prcow2
prcowpg
prdasian
prdisc
prdisflg
prdtcow1
prdtcow2
prdthsp
prdtind1
prdtind2
prdtocc1
prdtocc2
premp
premphrs
prempnot
prerelg
prernhly
prernwa
prexplf
prfamnum
prfamrel
prfamtyp
prftlf
prhernal
prhrusl
primind1
primind2
prinuyer
prioelg
prjobsea
prmarsta
prmjind1
prmjind2
prmjocc1
prmjocc2
prmjocgr
prnagpws
prnagws
prnlfsch
prnmchld
prpertyp
prpthrs
prptrea
prsjmj
prtage
prunedur
pruntype
prwernal
prwksch
prwkstat
prwntjob
ptdtrace
pthr
ptnmemp1
ptnmemp2
ptot
ptwk
puabsot
puafever
pubus1
pubus2ot
pudis
pudis1
pudis2
puhroff1
puhroff2
puhrot1
puhrot2
pujhdp1o
pulay
pulay6m
pulayavr
pulaydt
pulineno
pulk
pulkavr
pulkdk1
pulkdk2
pulkdk3
pulkdk4
pulkm2
pulkm3
pulkm4
pulkm5
pulkm6
pulkps1
pulkps2
pulkps3
pulkps4
pupelig
puretot
puslfprx
puwk
tratusr
tubwgt
ptcovid1
ptcovid2
ptcovid3
ptcovid4
ptcovid5w
pepar1
pepar2
pepar1typ
pepar2typ
prernmin
ptcovr1
ptcovr2
ptcovr3
ptcovr4
pxcovr1
pxcovr2
pxcovr3
pxcovr4
pttlwk
pttlwkhr
pxtlwk
pxtlwkhr
 using c:\atuscps_0324.dat, stringcols(1) ;

label variable gediv "Division";
label variable gemetsta "Metropolitan status (1990 definitions)";
label variable gepseucl "Scrambled pseudo primary sampling unit (PSU) cluster";
label variable gepseust "Scrambled pseudo primary sampling unit (PSU) collapsed stratum";
label variable gereg "Region";
label variable gestfips "Federal Processing Information Standards (FIPS) state code";
label variable gtcbsa "Specific metropolitan core based statistical area (CBSA) code";
label variable gtco "Federal Processing Standards (FIPS) county code";
label variable gtmetsta "Metropolitan status (2000 or 2010 definitions, see note)";
label variable hefaminc "Edited: Family Income";
label variable hehousut "Edited: type of housing unit";
label variable hephoneo "Edited: is a telephone interview acceptable?";
label variable hetelavl "Edited: is there a telephone elsewhere on which people in this household can be contacted?";
label variable hetelhhd "Edited: is there a telephone in this house/apartment?";
label variable hetenure "Edited: are your living quarters owned, rented for cash, or occupied without payment of cash rent?";
label variable hrhhid "Household ID (15-digit identifier)";
label variable hrhhid2 "Household ID part 2 (5-digit identifier)";
label variable hrhtype "Household type";
label variable hrintsta "Interview status";
label variable hrlonglk "Longitudinal link indicator";
label variable hrmis "Month in sample";
label variable hrmonth "Month of interview";
label variable hrnumhou "Total number of persons in the household (household members)";
label variable hrsample "Sample ID (4-character identifier)";
label variable hrsersuf "Serial suffix";
label variable hryear4 "Year of interview";
label variable hubus "Does anyone in this household have a business or a farm?";
label variable hubusl1 "PULINENO of farm or business owner (first owner)";
label variable hubusl2 "PULINENO of farm or business owner (second owner)";
label variable hubusl3 "PULINENO of farm or business owner (third owner)";
label variable hubusl4 "PULINENO of farm or business owner (fourth owner)";
label variable hufaminc "Family income ";
label variable hufinal "Final outcome code";
label variable huhhnum "Household number";
label variable huinttyp "Type of interview";
label variable huprscnt "Number of actual and attempted personal contacts";
label variable hurespli "PULINENO of the current respondent";
label variable huspnish "Spanish only language spoken by all members of household 15 years and older?";
label variable hxfaminc "HEFAMINC: allocation flag";
label variable peabspdo "Edited: are you being paid by your employer for any of the time off last week?";
label variable peabsrsn "Edited: what was the main reason you were absent from work last week?";
label variable peafever "Edited: did you ever serve on active duty in the U.S. Armed Forces?";
label variable peafnow "Edited: are you now in the Armed Forces?";
label variable peafwhen "Edited: was told you served on active duty in Armed Forces. When did you serve?";
label variable peafwhn1 "Edited: when did you serve in the Armed Forces? (first period)";
label variable peafwhn2 "Edited: when did you serve in the Armed Forces? (second period)";
label variable peafwhn3 "Edited: when did you serve in the Armed Forces? (third period)";
label variable peafwhn4 "Edited: when did you serve in the Armed Forces? (fourth period)";
label variable pecert1 "Edited: Does this person have a currently active professional certification or a state or industry license?";
label variable pecert2 "Edited: Were any of this person's certifications or licenses issued by the federal, state, or local government?";
label variable pecert3 "Edited: Earlier you told me that this person had a currently active professional certification or license. Is this certification or license required for the [job, main job, job from which person was on layoff, job from which person last worked]?";
label variable pecohab "Edited: PULINENO of cohabiting partner";
label variable pecyc "Edited: how many years of college credit have you completed?";
label variable pedadtyp "Edited: Is household child a biological, step or adopted child?";
label variable pedipged "Edited: how did you get your high school diploma?";
label variable pedisdrs "Edited: Does this person have difficulty dressing or bathing?";
label variable pedisear "Edited: Is this person deaf or does this person have serious difficulty hearing?";
label variable pediseye "Edited: Is this person blind or have serious difficulty seeing wearing glasses?";
label variable pedisout "Edited: Edited: does this person have difficulty doing errands alone?";
label variable pedisphy "Edited: Does this person have serious difficulty walking or climbing stairs?";
label variable pedisrem "Edited: does person have difficulty concentrating/remembering/making decisions?";
label variable pedw4wk "Edited: did you do any of this work during the last 4 weeks?";
label variable pedwavl "Edited: last week, could you have started a job if one had been offered?";
label variable pedwavr "Edited: why could you not have started a job if one had been offered last week?";
label variable pedwlko "Edited: did you look for work any time in the last 12 months?";
label variable pedwlkwk "Edited: and since you left that job or business have you looked for work?";
label variable pedwrsn "Edited: main reason you were not looking for work during the last 4 weeks?";
label variable pedwwk "Edited: did you actually work at a job or business during the last 12 months?";
label variable pedwwnto "Edited: do you currently want a job, either full or part time?";
label variable peeduca "Edited: highest level of school completed or the highest degree received?";
label variable peern "Edited: total weekly overtime earnings (2 implied decimals)";
label variable peerncov "Edited: on this job, are you covered by a union or employee assoc.";
label variable peernh1o "Edited: hrly pay rate (main job) exc. overtime, tips, & commissions (2 decimals)";
label variable peernh2 "Edited: hrly pay rate (main job) exc. overtime, tips, & commissions (2 decimals)";
label variable peernhro "Edited: how many hours do you usually work per week at this rate?";
label variable peernhry "Edited: hourly/non-hourly status";
label variable peernlab "Edited: on this job, are you a member of a labor union or of an employee assoc.?";
label variable peernper "Edited: main job, easiest to report earnings: hourly, weekly, annually, or other";
label variable peernrt "Edited: are you paid at an hourly rate on this job?";
label variable peernuot "Edited: do you usually receive overtime pay, tips, or commissions at your job?";
label variable peernwkp "Edited: how many weeks a year do you get paid?";
label variable pefntvty "Edited: in what country was your father born?";
label variable pegr6cor "Edited: did you complete six or more graduate or professional school courses?";
label variable pegrprof "Edited: since BA, taken any graduate/professional school courses for credit?";
label variable pehgcomp "Edited: highest grade of regular school you completed before receiving your GED?";
label variable pehract1 "Edited: last week, how many hours did you actually work at your main job?";
label variable pehract2 "Edited: last week, how many hours did you actually work at your other job(s)?";
label variable pehractt "Edited: total hours actually worked last week (sum of PEHRACT1 and PEHRACT2)";
label variable pehravl "Edited: last week, could you have worked full time if hours had been available?";
label variable pehrftpt "Edited: usually work > 35 hours per week at your job(s)/family business?";
label variable pehrrsn1 "Edited: what is your main reason for working part time?";
label variable pehrrsn2 "Edited: what is the main reason you do not want to work full time?";
label variable pehrrsn3 "Edited: what is the main reason you worked less than 35 hours last week?";
label variable pehrusl1 "Edited: how many hours per week do you usually work at your main job?";
label variable pehrusl2 "Edited: how many hours per week do you usually work at your other job(s)?";
label variable pehruslt "Edited: total hours usually worked per week (sum of PEHRUSL1 and PEHRUSL2)";
label variable pehrwant "Edited: do you want to work a full time work week of 35 hours or more per week?";
label variable pehspnon "Edited: are you Spanish, Hispanic, or Latino?";
label variable peio1cow "Edited: individual class of worker (main job)";
label variable peio1icd "Edited: industry code (main job)";
label variable peio1ocd "Edited: occupation code (main job)";
label variable peio2cow "Edited: individual class of worker (second job)";
label variable peio2icd "Edited: industry code (second job)";
label variable peio2ocd "Edited: occupation code (second job)";
label variable pejhrsn "Edited: what is the main reason you left your last job?";
label variable pejhwant "Edited: do you intend to look for work during the next 12 months?";
label variable pejhwko "Edited: have you worked at a job or business at any time in the last 12 months?";
label variable pelayavl "Edited: could you have returned to work during the last 7 days if recalled?";
label variable pelaydur "Edited: duration of layoff (number of weeks)";
label variable pelayfto "Edited: the job from which you are on layoff full time job of >=35 hours/week?";
label variable pelaylk "Edited: though you are to be called back to work, looking for work last 4 weeks?";
label variable pelkavl "Edited: could you have started a job in the last 7 days if one had been offered?";
label variable pelkdur "Edited: duration of job seeking (number of weeks)";
label variable pelkfto "Edited: are you seeking a full time or part time job?";
label variable pelkll1o "Edited: before you started looking for work, what were you doing?";
label variable pelkll2o "Edited: did you lose or quit that job, or was it a temporary job that ended?";
label variable pelklwo "Edited: when did you last work?";
label variable pelkm1 "Edited: things you have done to find work during the last 4 weeks? (1st method)";
label variable pelndad "Edited: PULINENO of father";
label variable pelnmom "Edited: PULINENO of mother";
label variable pemaritl "Edited: are you now married, widowed, divorced, separated, or never married?";
label variable pemjnum "Edited: altogether, how many jobs did you have?";
label variable pemjot "Edited: in the last seven days, did you have more than one job?";
label variable pemlr "Edited: monthly labor force recode";
label variable pemntvty "Edited: in what country was your mother born?";
label variable pemomtyp "Edited: Is household child a biological, step, or adopted child?";
label variable pems123 "Edited: was your master's degree program a 1-year, 2-year, or 3-year program?";
label variable penatvty "Edited: in what country were you born?";
label variable penlfact "Edited: what best describes your situation at this time? (Not in labor force)";
label variable penlfjh "Edited: when did you last work at a job or business?";
label variable penlfret "Edited: are you retired from a job or business?";
label variable peparent "Edited: PULINENO of parent";
label variable pepdemp1 "Does this person usually have any paid employees?";
label variable pepdemp2 "Does this person usually have any paid employees?";
label variable peret1 "Edited: do you currently want a job, either full or part time?";
label variable perrp "Edited: how is this person related to you?";
label variable peschenr "Edited: last week, were you enrolled in a high school, college, or university?";
label variable peschft "Edited: are you enrolled in school as a full-time or part-time student?";
label variable peschlvl "Edited: would that be high school, college, or university?";
label variable pesex "Edited: sex";
label variable pespouse "Edited: PULINENO of spouse";
label variable prabsrea "Reason not at work by pay status";
label variable pragna "Agricultural/non-agricultural industry";
label variable prcitshp "Citizenship status";
label variable prcivlf "Civilian labor force";
label variable prcow1 "Class of worker recode (main job)";
label variable prcow2 "Class of worker recode (second job)";
label variable prcowpg "Class of worker - private or government";
label variable prdasian "Detailed Asian race recode";
label variable prdisc "Discouraged worker recode";
label variable prdisflg "Does this person have any of these disability conditions?";
label variable prdtcow1 "Detailed class of worker recode (main job)";
label variable prdtcow2 "Detailed class of worker recode (second job)";
label variable prdthsp "Detailed Hispanic origin group";
label variable prdtind1 "Detailed industry recode (main job)";
label variable prdtind2 "Detailed industry recode (second job)";
label variable prdtocc1 "Detailed occupation recode (main job)";
label variable prdtocc2 "Detailed occupation recode (second job)";
label variable premp "Employed persons recode";
label variable premphrs "Reason not at work or hours at work";
label variable prempnot "Employed, unemployed, or not in the labor force";
label variable prerelg "Earnings edit eligibility flag";
label variable prernhly "Hourly earnings (2 implied decimals)";
label variable prernwa "Weekly earnings (2 implied decimals)";
label variable prexplf "Experienced labor force employment";
label variable prfamnum "Family number recode";
label variable prfamrel "Family relationship code";
label variable prfamtyp "Family type recode";
label variable prftlf "Full time labor force";
label variable prhernal "PRERNHLY: allocation flag";
label variable prhrusl "Usual hours worked weekly";
label variable primind1 "Intermediate industry recode (main job)";
label variable primind2 "Intermediate industry recode (second job)";
label variable prinuyer "Immigrant's year of entry into the U.S.";
label variable prioelg "Industry and occupation edit eligibility flag";
label variable prjobsea "Job search recode";
label variable prmarsta "Marital status based on Armed Forces participation";
label variable prmjind1 "Major industry recode (main job)";
label variable prmjind2 "Major industry recode (second job)";
label variable prmjocc1 "Major occupation recode (main job)";
label variable prmjocc2 "Major occupation recode (second job)";
label variable prmjocgr "Major occupation categories (main job)";
label variable prnagpws "Non-agricultural private wage and salary workers recode";
label variable prnagws "Non-agricultural wage and salary workers recode";
label variable prnlfsch "Not in labor force activity - in school or not in school";
label variable prnmchld "Number of own children < 18 years of age";
label variable prpertyp "Type of person recode";
label variable prpthrs "At work 1-34 hours by hours at work";
label variable prptrea "Detailed reason for part time work";
label variable prsjmj "Single/multiple jobholder";
label variable prtage "Age";
label variable prunedur "Duration of unemployment (number of weeks)";
label variable pruntype "Reason for unemployment";
label variable prwernal "PRERNWA: allocation flag";
label variable prwksch "Labor force by time worked or lost";
label variable prwkstat "Full time or part time work status";
label variable prwntjob "Not in labor force recode - want a job or other not in labor force";
label variable ptdtrace "Race (topcoded)";
label variable pthr "Hourly pay topcode flag";
label variable ptnmemp1 "Excluding all owners, how many paid employees does this person usually have?";
label variable ptnmemp2 "Excluding all owners, how many paid employees does this person usually have?";
label variable ptot "Weekly overtime amount topcode flag";
label variable ptwk "Weekly earnings topcode flag";
label variable puabsot "In the last seven days, did you have a job either full or part time?";
label variable puafever "Did you ever serve on active duty in the U.S. Armed Forces?";
label variable pubus1 "Last week, did you do any unpaid work in the family business or farm?";
label variable pubus2ot "Do you receive any payments or profits from the business?";
label variable pudis "Disability continues to prevent you from accepting work in next 6 months?";
label variable pudis1 "Disability prevents you from accepting work in the next 6 months?";
label variable pudis2 "Disability prevents you from accepting work in the next 6 months?";
label variable puhroff1 "Last week, lose or take off any hours from your job for any reason?";
label variable puhroff2 "How many hours did you take off?";
label variable puhrot1 "Last week, did you work any overtime or extra hours? (main job)";
label variable puhrot2 "How many additional hours did you work?";
label variable pujhdp1o "Did you do any of this work in the last 4 weeks?";
label variable pulay "During the last seven days, were you on layoff from a job?";
label variable pulay6m "Given any indication that you will be recalled to work within the next 6 months?";
label variable pulayavr "Why could you not have started a job in the last week?";
label variable pulaydt "Has your employer given you a date to return to work? (to layoff job)";
label variable pulineno "Person line number";
label variable pulk "Have you been doing anything to find work during the last 4 weeks?";
label variable pulkavr "Why could you not have started a job last week?";
label variable pulkdk1 "Said trying to find work. How did you go about looking? (1st method)";
label variable pulkdk2 "PULKDK1 text: (second method)";
label variable pulkdk3 "PULKDK1 text: (third method)";
label variable pulkdk4 "PULKDK1 text: (fourth method)";
label variable pulkm2 "Things you have done to find work during the last 4 weeks? (second method)";
label variable pulkm3 "PULKM2 text: (third method)";
label variable pulkm4 "PULKM2 text: (fourth method)";
label variable pulkm5 "PULKM2 text: (fifth method)";
label variable pulkm6 "PULKM2 text: (sixth method)";
label variable pulkps1 "Can you tell me more about what you did to search for work? (first method)";
label variable pulkps2 "PULKPS1 text: (second method)";
label variable pulkps3 "PULKPS1 text: (third method)";
label variable pulkps4 "PULKPS1 text: (fourth method)";
label variable pupelig "Interview status of each person in the household";
label variable puretot "Last month you were reported to be retired. Are you still retired?";
label variable puslfprx "Labor force information collected by self or proxy response";
label variable puwk "Last week, did you do any work for either pay or profit?";
label variable tratusr "ATUS respondent";
label variable tubwgt "ATUS base weight";
label variable tucaseid "ATUS Case ID (14-digit identifier)";
label variable tulineno "ATUS person line number";
label variable ptcovid1 "At any time in the LAST 4 weeks, did you telework or work at home for pay BECAUSE OF THE CORONAVIRUS PANDEMIC?";
label variable ptcovid2 "At any time in the LAST 4 WEEKS, were you unable to work because your EMPLOYER CLOSED OR LOST BUSINESS due to the Coronavirus?";
label variable ptcovid3 "Did you receive any pay from your EMPLOYER for the hours you DID NOT work in the last 4 weeks?";
label variable ptcovid4 "Did the Coronavirus pandemic prevent you from looking for work in the LAST 4 WEEKS?";
label variable ptcovid5w "At any time in the last 4 weeks, did you need medical care for something other than Coronavirus, but not get it because of the Coronavirus pandemic?";
label variable pepar1 "Edited: PULINENO of first parent";
label variable pepar2 "Edited: PULINENO of second parent";
label variable pepar1typ "Edited: Type of PEPAR1";
label variable pepar2typ "Edited: Type of PEPAR2";
label variable prernmin "Federally mandated minimum wage rate flag";
label variable ptcovr1 "At any time LAST WEEK did (you/name) telework or work at home for pay";
label variable ptcovr2 "LAST WEEK, (you/name) worked (# hours worked last week at all jobs) hours (total/at all jobs). How many of these hours did (you/name) telework or work at home for pay";
label variable ptcovr3 "Did (you/name) telework or work at home for pay in February 2020 before the COVID-19 pandemic started";
label variable ptcovr4 "LAST WEEK, did (you/name) do more, less, or the same amount of telework or work at home for pay as in February 2020 (before the COVID-19 pandemic)?";
label variable pxcovr1 "PTCOVR1: allocation flag";
label variable pxcovr2 "PTCOVR2: allocation flag";
label variable pxcovr3 "PTCOVR3: allocation flag";
label variable pxcovr4 "PTCOVR4: allocation flag";
label variable pttlwk "Telework at home";
label variable pttlwkhr "Number of hours teleworked";
label variable pxtlwk "PTTLWK: allocation flag";
label variable pxtlwkhr "PTTLWKHR: allocation flag";

label define labelgediv
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "New England"
2 "Middle Atlantic"
3 "East North Central"
4 "West North Central"
5 "South Atlantic"
6 "East South Central"
7 "West South Central"
8 "Mountain"
9 "Pacific"
;
label define labelgereg
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Northeast"
2 "Midwest (formerly North Central)"
3 "South"
4 "West"
;
label define labelgemetsta
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Metropolitan"
2 "Non-metropolitan"
3 "Not identified"
;
label define labelgtmetsta
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Metropolitan"
2 "Non-metropolitan"
3 "Not identified"
;
label define labelhefaminc
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Less than $5,000"
2 "$5,000 to $7,499"
3 "$7,500 to $9,999"
4 "$10,000 to $12,499"
5 "$12,500 to $14,999"
6 "$15,000 to $19,999"
7 "$20,000 to $24,999"
8 "$25,000 to $29,999"
9 "$30,000 to $34,999"
10 "$35,000 to $39,999"
11 "$40,000 to $49,999"
12 "$50,000 to $59,999"
13 "$60,000 to $74,999"
14 "$75,000 to $99,999"
15 "$100,000 to $149,999"
16 "$150,000 and over"
;
label define labelhehousut
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "House, apartment, flat"
2 "Housing unit in nontransient hotel, motel, etc."
3 "Housing unit permanent in transient hotel, motel"
4 "Housing unit in rooming house"
5 "Mobile home or trailer with no permanent room added"
6 "Mobile home or trailer with 1 or more rooms added"
7 "Housing unit not specified above"
8 "Quarters not housing unit in rooming/boarding house"
9 "Unit not permanent in transient hotel/motel"
10 "Unoccupied tent site or trailer site"
11 "Student quarters in college dorm"
12 "Other unit not specified above"
;
label define labelhephoneo
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Unknown"
1 "Yes"
2 "No"
;
label define labelhetelavl
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelhetelhhd
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelhetenure
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Owned or being bought by a household member"
2 "Rented for cash"
3 "Occupied without payment of cash rent"
;
label define labelhrhtype
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Husband/wife primary family (neither Armed Forces)"
2 "Husband/wife primary family (either/both Armed Forces)"
3 "Unmarried civilian male - primary family householder"
4 "Unmarried civilian female - primary family householder"
5 "Primary family householder - respondent in Armed Forces, unmarried"
6 "Civilian male primary individual"
7 "Civilian female primary individual"
8 "Primary individual householder - respondent in Armed Forces"
9 "Group quarters with family"
10 "Group quarters without family"
;
label define labelhrintsta
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Interview"
;
label define labelhrlonglk
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Replacement household - no link to prior month"
2 "Link to previous month"
;
label define labelhrmis
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
8 "Month in sample 8 (MIS-8)"
;
label define labelhubus
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelhufaminc
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Less than $5,000"
2 "$5,000 to $7,499"
3 "$7,500 to $9,999"
4 "$10,000 to $12,499"
5 "$12,500 to $14,999"
6 "$15,000 to $19,999"
7 "$20,000 to $24,999"
8 "$25,000 to $29,999"
9 "$30,000 to $34,999"
10 "$35,000 to $39,999"
11 "$40,000 to $49,999"
12 "$50,000 to $59,999"
13 "$60,000 to $74,999"
14 "$75,000 to $99,999"
15 "$100,000 to $149,999"
16 "$150,000 and over"
;
label define labelhufinal
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Fully complete CATI"
2 "Partially complete CATI"
4 "Partial CATI - not complete at closeout"
5 "Labor force complete, supplement incomplete, CATI"
201 "Fully complete CAPI"
203 "Sufficient partial CAPI - pre-closeout"
204 "Sufficient partial CAPI - at closeout"
205 "Labor force complete, supplement incomplete, CAPI"
;
label define labelhuinttyp
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Personal"
2 "Telephone"
;
label define labelhuspnish
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Spanish only language spoken"
;
label define labelhxfaminc
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Value - No Change"
1 "Blank - No Change"
2 "Don`t Know - No Change"
3 "Refused - No Change"
10 "Value To Value"
11 "Blank To Value"
12 "Don`t Know To Value"
13 "Refused To Value"
20 "Value To Longitudinal Value"
21 "Blank To Longitudinal Value"
22 "Don`t Know To Longitudinal Value"
23 "Refused To Longitudinal Value"
30 "Value To Allocated Value Long."
31 "Blank To Allocated Value Long."
32 "Don`t Know To Allocated Value Long."
33 "Refused To Allocated Value Long."
40 "Value To Allocated Value"
41 "Blank To Allocated Value"
42 "Don`t Know To Allocated Value"
43 "Refused To Allocated Value"
50 "Value To Blank"
52 "Don`t Know To Blank"
53 "Refused To Blank"
;
label define labelpeabspdo
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpeabsrsn
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "On layoff"
2 "Slack work/business conditions"
3 "Waiting for a new job to begin"
4 "Vacation/personal days"
5 "Own illness/injury/medical problems"
6 "Childcare problems"
7 "Other family/personal obligation"
8 "Maternity/paternity leave"
9 "Labor dispute"
10 "Weather affected job"
11 "School/training"
12 "Civic/military duty"
13 "Does not work in the business"
14 "Other"
;
label define labelpeafever
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpeafnow
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpeafwhen
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Vietnam Era (8/64-4/75)"
2 "Korean War (6/50-1/55)"
3 "World War II (9/40-7/47)"
4 "World War I (4/17-11/18)"
5 "Other service (all other periods)"
6 "Non veteran"
;
label define labelpeafwhn1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "September 2001 or later"
2 "August 1990 to August 2001"
3 "May 1975 to July 1990"
4 "Vietnam Era (August 1964 to April 1975)"
5 "February 1955 to July 1964"
6 "Korean War (July 1950 to January 1955)"
7 "January 1947 to June 1950"
8 "World War II (December 1941 to December 1946)"
9 "November 1941 or earlier"
;
label define labelpeafwhn2
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "September 2001 or later"
2 "August 1990 to August 2001"
3 "May 1975 to July 1990"
4 "Vietnam Era (August 1964 to April 1975)"
5 "February 1955 to July 1964"
6 "Korean War (July 1950 to January 1955)"
7 "January 1947 to June 1950"
8 "World War II (December 1941 to December 1946)"
9 "November 1941 or earlier"
;
label define labelpeafwhn3
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "September 2001 or later"
2 "August 1990 to August 2001"
3 "May 1975 to July 1990"
4 "Vietnam Era (August 1964 to April 1975)"
5 "February 1955 to July 1964"
6 "Korean War (July 1950 to January 1955)"
7 "January 1947 to June 1950"
8 "World War II (December 1941 to December 1946)"
9 "November 1941 or earlier"
;
label define labelpeafwhn4
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "September 2001 or later"
2 "August 1990 to August 2001"
3 "May 1975 to July 1990"
4 "Vietnam Era (August 1964 to April 1975)"
5 "February 1955 to July 1964"
6 "Korean War (July 1950 to January 1955)"
7 "January 1947 to June 1950"
8 "World War II (December 1941 to December 1946)"
9 "November 1941 or earlier"
;
label define labelpecert1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Yes"
1 "No"
;
label define labelpecert2
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Yes"
1 "No"
;
label define labelpecert3
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Yes"
1 "No"
;
label define labelpecyc
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Less than 1 year (includes 0 years completed)"
2 "The first or freshman year"
3 "The second or sophomore year"
4 "The third or junior year"
5 "Four or more years"
;
label define labelpedadtyp
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Biological"
2 "Step"
3 "Adopted"
;
label define labelpedipged
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Graduation from high school"
2 "GED or other equivalent"
;
label define labelpedisdrs
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpedisear
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpediseye
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpedisout
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpedisphy
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpedisrem
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpedw4wk
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpedwavl
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpedwavr
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Own temporary illness"
2 "Going to school"
3 "Other"
;
label define labelpedwlko
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpedwlkwk
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpedwrsn
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Believes no work available in area of expertise"
2 "Couldn`t find any work"
3 "Lacks necessary schooling/training"
4 "Employers think too young or too old"
5 "Other types of discrimination"
6 "Can`t arrange childcare"
7 "Family responsibilities"
8 "In school or other training"
9 "Ill-health, physical disability"
10 "Transportation problems"
11 "Other"
;
label define labelpedwwk
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpedwwnto
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes, or maybe/it depends"
2 "No"
3 "Retired"
4 "Disabled"
5 "Unable to work"
;
label define labelpeeduca
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
31 "Less than 1st grade"
32 "1st, 2nd, 3rd, or 4th grade"
33 "5th or 6th grade"
34 "7th or 8th grade"
35 "9th grade"
36 "10th grade"
37 "11th grade"
38 "12th grade - no diploma"
39 "High school graduate - diploma or equivalent (GED)"
40 "Some college but no degree"
41 "Associate degree - occupational/vocational"
42 "Associate degree - academic program"
43 "Bachelor's degree (BA, AB, BS, etc.)"
44 "Master's degree (MA, MS, MEng, MEd, MSW, etc.)"
45 "Professional school degree (MD, DDS, DVM, etc.)"
46 "Doctoral degree (PhD, EdD, etc.)"
;
label define labelpeerncov
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpeernhry
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Hourly worker"
2 "Non-hourly worker"
;
label define labelpeernlab
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpeernper
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Hourly"
2 "Weekly"
3 "Bi-weekly"
4 "Twice monthly"
5 "Monthly"
6 "Annually"
7 "Other"
;
label define labelpeernrt
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpeernuot
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
/* Stata will not process these values.
label define labelpefntvty
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
57 "United States"
66 "Guam"
72 "Puerto Rico"
73 "Puerto Rico"
78 "U.S. Virgin Islands"
96 "U.S. Outlying Area"
100-554 "Foreign country or at sea"
555 "Abroad, country not known"
;
*/
label define labelpegr6cor
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpegrprof
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpehgcomp
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Less than 1st grade"
2 "1st, 2nd, 3rd, or 4th grade"
3 "5th or 6th grade"
4 "7th or 8th grade"
5 "9th grade"
6 "10th grade"
7 "11th grade"
8 "12th grade - no diploma"
;
label define labelpehravl
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpehrftpt
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Full time"
2 "Part time"
3 "Hours vary"
;
label define labelpehrrsn1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Slack work/business conditions"
2 "Could only find part time work"
3 "Seasonal work"
4 "Childcare problems"
5 "Other family/personal obligations"
6 "Health/medical limitations"
7 "School/training"
8 "Retired/Social Security limit on earnings"
9 "Full time work week is less than 35 hours"
10 "Other"
;
label define labelpehrrsn2
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Childcare problems"
2 "Other family/personal obligations"
3 "Health/medical limitations"
4 "School/training"
5 "Retired/Social Security limit on earnings"
6 "Full time work week is less than 35 hours"
7 "Other"
;
label define labelpehrrsn3
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Slack work/business conditions"
2 "Seasonal work"
3 "Job started or ended during week"
4 "Vacation/personal day"
5 "Own illness/injury/medical appointment"
6 "Holiday (legal or religious)"
7 "Childcare problems"
8 "Other family/personal obligations"
9 "Labor dispute"
10 "Weather affected job"
11 "School/training"
12 "Civic/military duty"
13 "Other reason"
;
label define labelpehrwant
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
3 "Regular hours are full time"
;
label define labelpehspnon
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Hispanic"
2 "Non-Hispanic"
;
label define labelpeio1cow
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Government, federal"
2 "Government, state"
3 "Government, local"
4 "Private, for profit"
5 "Private, nonprofit"
6 "Self-employed, incorporated"
7 "Self-employed, unincorporated"
8 "Without pay"
;
label define labelpeio2cow
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Government, federal"
2 "Government, state"
3 "Government, local"
4 "Private, for profit"
5 "Private, nonprofit"
6 "Self-employed, incorporated"
7 "Self-employed, unincorporated"
8 "Without pay"
;
label define labelpejhrsn
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Personal/family (including pregnancy)"
2 "Return to school"
3 "Health"
4 "Retirement or old age"
5 "Temporary, seasonal, or intermittent job completed"
6 "Slack work/business conditions"
7 "Unsatisfactory work arrangements (hours, pay, etc.)"
8 "Other"
;
label define labelpejhwant
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes, or it depends"
2 "No"
;
label define labelpejhwko
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpelayavl
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpelayfto
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpelaylk
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpelkavl
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpelkfto
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
3 "Doesn't matter"
;
label define labelpelkll1o
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Working"
2 "School"
3 "Left military service"
4 "Something else"
;
label define labelpelkll2o
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Lost job"
2 "Quit job"
3 "Temporary job ended"
;
label define labelpelklwo
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Within the last 12 months"
2 "More than 12 months ago"
3 "Never worked"
;
label define labelpelkm1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Contacted employer directly/interview"
2 "Contacted public employment agency"
3 "Contacted private employment agency"
4 "Contacted friends or relatives"
5 "Contacted school/university employment center"
6 "Sent out resumes/filled out applications"
7 "Checked union/professional registers"
8 "Placed or answered ads"
9 "Other active"
10 "Looked at ads"
11 "Attended job training programs/courses"
12 "Nothing"
13 "Other passive"
;
label define labelpemaritl
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Married - spouse present"
2 "Married - spouse absent"
3 "Widowed"
4 "Divorced"
5 "Separated"
6 "Never married"
;
label define labelpemjnum
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
2 "Two jobs"
3 "Three jobs"
4 "Four or more jobs"
;
label define labelpemjot
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpemlr
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Employed - at work"
2 "Employed - absent"
3 "Unemployed - on layoff"
4 "Unemployed - looking"
5 "Not in labor force - retired"
6 "Not in labor force - disabled"
7 "Not in labor force - other"
;
/* Stata will not process these values.
label define labelpemntvty
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
57 "United States"
66 "Guam"
72 "Puerto Rico"
73 "Puerto Rico"
78 "U.S. Virgin Islands"
96 "U.S. Outlying Area"
100-554 "Foreign country or at sea"
555 "Abroad, country not known"
;
*/
label define labelpems123
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "One-year program"
2 "Two-year program"
3 "Three-year program (or longer)"
;
/* Stata will not process these values.
label define labelpenatvty
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
57 "United States"
66 "Guam"
72 "Puerto Rico"
73 "Puerto Rico"
78 "U.S. Virgin Islands"
96 "U.S. Outlying Area"
100-554 "Foreign country or at sea"
555 "Abroad, country not known"
;
*/
label define labelpenlfact
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Disabled"
2 "Ill"
3 "In school"
4 "Taking care of house or family"
5 "In retirement"
6 "Something else/other"
;
label define labelpenlfjh
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Within the last 12 months"
2 "More than 12 months ago"
3 "Never worked"
;
label define labelpenlfret
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpepdemp1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpepdemp2
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelperet1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
3 "Has a job"
;
label define labelperrp
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Reference person living with relatives (before 2020)"
2 "Reference person living without relatives (before 2020)"
3 "Spouse (before 2020)"
4 "Own child (before 2020)"
5 "Grandchild (before 2020)"
6 "Parent (before 2020)"
7 "Brother/sister (before 2020)"
8 "Other relative of reference person (before 2020)"
9 "Foster child (before 2020)"
10 "Nonrelative of reference person living with relatives (before 2020)"
12 "Nonrelative of reference person living without relatives (before 2020)"
13 "Unmarried partner living with relatives (before 2020)"
14 "Unmarried partner living without relatives (before 2020)"
15 "Housemate/roommate living with relatives (before 2020)"
16 "Housemate/roommate living without relatives (before 2020)"
17 "Roomer/boarder living with relatives (before 2020)"
18 "Roomer/boarder living without relatives (before 2020)"
40 "Reference person living with relatives"
41 "Reference person living without relatives"
42 "Opposite sex spouse"
43 "Opposite sex partner living with relatives"
44 "Opposite sex partner living without relatives"
45 "Same sex spouse"
46 "Same sex partner living with relatives"
47 "Same sex partner living without relatives"
48 "Own child"
49 "Grandchild"
50 "Parent"
51 "Brother/sister"
52 "Other relative of reference person"
53 "Foster child"
54 "Housemate/roommate living with relatives"
55 "Housemate/roommate living without relatives"
56 "Roomer/Boarder living with relatives"
57 "Roomer/boarder living without relatives"
58 "Nonrelative of reference person living with relatives"
59 "Nonrelative of reference person living without relatives"
;
label define labelpeschenr
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpeschft
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Full time"
2 "Part time"
;
label define labelpeschlvl
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "High school"
2 "College or university"
;
label define labelpesex
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Male"
2 "Female"
;
label define labelprabsrea
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Full time paid - vacation"
2 "Full time paid - own illness"
3 "Full time paid - childcare problems"
4 "Full time paid - other family/personal obligation"
5 "Full time paid - maternity/paternity leave"
6 "Full time paid - labor dispute"
7 "Full time paid - weather affected job"
8 "Full time paid - school/training"
9 "Full time paid - civic/military duty"
10 "Full time paid - other"
11 "Full time unpaid - vacation"
12 "Full time unpaid - own illness"
13 "Full time unpaid - childcare problems"
14 "Full time unpaid - other family/personal obligation"
15 "Full time unpaid - maternity/paternity leave"
16 "Full time unpaid - labor dispute"
17 "Full time unpaid - weather affected job"
18 "Full time unpaid - school/training"
19 "Full time unpaid - civic/military duty"
20 "Full time unpaid - other"
21 "Part time paid - vacation"
22 "Part time paid - own illness"
23 "Part time paid - childcare problems"
24 "Part time paid - other family/personal obligation"
25 "Part time paid - maternity/paternity leave"
26 "Part time paid - labor dispute"
27 "Part time paid - weather affected job"
28 "Part time paid - school/training"
29 "Part time paid - civic/military duty"
30 "Part time paid - other"
31 "Part time unpaid - vacation"
32 "Part time unpaid - own illness"
33 "Part time unpaid - childcare problems"
34 "Part time unpaid - other family/personal obligation"
35 "Part time unpaid - maternity/paternity leave"
36 "Part time unpaid - labor dispute"
37 "Part time unpaid - weather affected job"
38 "Part time unpaid - school/training"
39 "Part time unpaid - civic/military duty"
40 "Part time unpaid - other"
;
label define labelpragna
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Agricultural"
2 "Non-agricultural"
;
label define labelprcitshp
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Native, born in United States"
2 "Native, born in Puerto Rico or U.S. Outlying Area"
3 "Native, born abroad of American parent or parents"
4 "Foreign born, U.S. citizen by naturalization"
5 "Foreign born, not a U.S. citizen"
;
label define labelprcivlf
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "In civilian labor force"
2 "Not in civilian labor force"
;
label define labelprcow1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Federal government"
2 "State government"
3 "Local government"
4 "Private (including incorporated self-employed)"
5 "Self-employed, unincorporated"
6 "Without pay"
;
label define labelprcow2
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Federal government"
2 "State government"
3 "Local government"
4 "Private (including incorporated self-employed)"
5 "Self-employed, unincorporated"
6 "Without pay"
;
label define labelprcowpg
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Private"
2 "Government"
;
label define labelprdasian
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Asian Indian"
2 "Chinese"
3 "Filipino"
4 "Japanese"
5 "Korean"
6 "Vietnamese"
7 "Other"
;
label define labelprdisc
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Discouraged worker"
2 "Conditionally interested"
3 "Not available"
;
label define labelprdisflg
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelprdtcow1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Agricultural, wage/salary, private"
2 "Agricultural, wage/salary, government"
3 "Agricultural, self-employed"
4 "Agricultural, unpaid"
5 "Non-agricultural, wage/salary, private households"
6 "Non-agricultural, wage/salary, other private"
7 "Non-agricultural, wage/salary, federal government"
8 "Non-agricultural, wage/salary, state government"
9 "Non-agricultural, wage/salary, local government"
10 "Non-agricultural, self-employed"
11 "Non-agricultural, unpaid"
;
label define labelprdtcow2
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Agricultural, wage/salary, private"
2 "Agricultural, wage/salary, government"
3 "Agricultural, self-employed"
4 "Agricultural, unpaid"
5 "Non-agricultural, wage/salary, private households"
6 "Non-agricultural, wage/salary, other private"
7 "Non-agricultural, wage/salary, federal government"
8 "Non-agricultural, wage/salary, state government"
9 "Non-agricultural, wage/salary, local government"
10 "Non-agricultural, self-employed"
11 "Non-agricultural, unpaid"
;
label define labelprdthsp
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Mexican"
2 "Puerto Rican"
3 "Cuban"
4 "Central/South American (before 2014) or Dominican (starting in 2014)"
5 "Other Spanish (before 2014) or Salvadoran (starting in 2014)"
6 "Other Central American, excluding Salvadoran (starting in 2014)"
7 "South American (starting in 2014)"
8 "Other Spanish (starting in 2014)"
;
label define labelprdtind1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1  "Agriculture"
2  "Forestry, logging, fishing, hunting, and trapping"
3  "Mining"
4  "Construction"
5  "Nonmetallic mineral product manufacturing"
6  "Primary metals and fabricated metal products"
7  "Machinery manufacturing"
8  "Computer and electronic product manufacturing"
9  "Electrical equipment, appliance manufacturing"
10 "Transportation equipment manufacturing"
11 "Wood product manufacturing"
12 "Furniture and fixtures manufacturing"
13 "Miscellaneous and not specified manufacturing"
14 "Food manufacturing"
15 "Beverage and tobacco product manufacturing"
16 "Textile, apparel, and leather manufacturing"
17 "Paper manufacturing and printing"
18 "Petroleum and coal products manufacturing"
19 "Chemical manufacturing"
20 "Plastics and rubber products manufacturing"
21 "Wholesale trade"
22 "Retail trade"
23 "Transportation and warehousing"
24 "Utilities"
25 "Publishing industries (except internet)"
26 "Motion picture and sound recording industries"
27 "Broadcasting (except internet)"
28 "Internet publishing and broadcasting"
29 "Telecommunications"
30 "Internet service providers and data processing services"
31 "Other information services"
32 "Finance"
33 "Insurance"
34 "Real estate"
35 "Rental and leasing services"
36 "Professional, scientific, and technical services"
37 "Management of companies and enterprises"
38 "Administrative and support services"
39 "Waste management and remediation services"
40 "Educational services"
41 "Hospitals"
42 "Health care services, except hospitals"
43 "Social assistance"
44 "Arts, entertainment, and recreation"
45 "Traveler accommodation"
46 "Food services and drinking places"
47 "Repair and maintenance"
48 "Personal and laundry services"
49 "Membership associations and organizations"
50 "Private households"
51 "Public administration"
52 "Armed Forces"
;
label define labelprdtind2
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1  "Agriculture"
2  "Forestry, logging, fishing, hunting, and trapping"
3  "Mining"
4  "Construction"
5  "Nonmetallic mineral product manufacturing"
6  "Primary metals and fabricated metal products"
7  "Machinery manufacturing"
8  "Computer and electronic product manufacturing"
9  "Electrical equipment, appliance manufacturing"
10 "Transportation equipment manufacturing"
11 "Wood product manufacturing"
12 "Furniture and fixtures manufacturing"
13 "Miscellaneous and not specified manufacturing"
14 "Food manufacturing"
15 "Beverage and tobacco product manufacturing"
16 "Textile, apparel, and leather manufacturing"
17 "Paper manufacturing and printing"
18 "Petroleum and coal products manufacturing"
19 "Chemical manufacturing"
20 "Plastics and rubber products manufacturing"
21 "Wholesale trade"
22 "Retail trade"
23 "Transportation and warehousing"
24 "Utilities"
25 "Publishing industries (except internet)"
26 "Motion picture and sound recording industries"
27 "Broadcasting (except internet)"
28 "Internet publishing and broadcasting"
29 "Telecommunications"
30 "Internet service providers and data processing services"
31 "Other information services"
32 "Finance"
33 "Insurance"
34 "Real estate"
35 "Rental and leasing services"
36 "Professional, scientific, and technical services"
37 "Management of companies and enterprises"
38 "Administrative and support services"
39 "Waste management and remediation services"
40 "Educational services"
41 "Hospitals"
42 "Health care services, except hospitals"
43 "Social assistance"
44 "Arts, entertainment, and recreation"
45 "Traveler accommodation"
46 "Food services and drinking places"
47 "Repair and maintenance"
48 "Personal and laundry services"
49 "Membership associations and organizations"
50 "Private households"
51 "Public administration"
52 "Armed Forces"
;
label define labelprdtocc1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Management occupations"
2 "Business and financial operations occupations"
3 "Computer and mathematical science occupations"
4 "Architecture and engineering occupations"
5 "Life, physical, and social science occupations"
6 "Community and social service occupations"
7 "Legal occupations"
8 "Education, training, and library occupations"
9 "Arts, design, entertainment, sports, and media occupations"
10 "Healthcare practitioner and technical occupations"
11 "Healthcare support occupations"
12 "Protective service occupations"
13 "Food preparation and serving related occupations"
14 "Building and grounds cleaning and maintenance occupations"
15 "Personal care and service occupations"
16 "Sales and related occupations"
17 "Office and administrative support occupations"
18 "Farming, fishing, and forestry occupations"
19 "Construction and extraction occupations"
20 "Installation, maintenance, and repair occupations"
21 "Production occupations"
22 "Transportation and material moving occupations"
23 "Armed Forces"
;
label define labelprdtocc2
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Management occupations"
2 "Business and financial operations occupations"
3 "Computer and mathematical science occupations"
4 "Architecture and engineering occupations"
5 "Life, physical, and social science occupations"
6 "Community and social service occupations"
7 "Legal occupations"
8 "Education, training, and library occupations"
9 "Arts, design, entertainment, sports, and media occupations"
10 "Healthcare practitioner and technical occupations"
11 "Healthcare support occupations"
12 "Protective service occupations"
13 "Food preparation and serving related occupations"
14 "Building and grounds cleaning and maintenance occupations"
15 "Personal care and service occupations"
16 "Sales and related occupations"
17 "Office and administrative support occupations"
18 "Farming, fishing, and forestry occupations"
19 "Construction and extraction occupations"
20 "Installation, maintenance, and repair occupations"
21 "Production occupations"
22 "Transportation and material moving occupations"
23 "Armed Forces"
;
label define labelpremp
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Employed persons (excluding agriculture and private households)"
;
label define labelpremphrs
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Unemployed and not in the labor force"
1 "With job, not at work - illness"
2 "With job, not at work - vacation"
3 "With job, not at work - weather affected job"
4 "With job, not at work - labor dispute"
5 "With job, not at work - childcare problems"
6 "With job, not at work - family/personal obligation"
7 "With job, not at work - maternity/paternity"
8 "With job, not at work - school/training"
9 "With job, not at work - civic/military duty"
10 "With job, not at work - does not work in business"
11 "With job, not at work - other"
12 "At work, 1-4 hours"
13 "At work, 5-14 hours"
14 "At work, 15-21 hours"
15 "At work, 22-29 hours"
16 "At work, 30-34 hours"
17 "At work, 35-39 hours"
18 "At work, 40 hours"
19 "At work, 41-47 hours"
20 "At work, 48 hours"
21 "At work, 49-59 hours"
22 "At work, 60 hours or more"
;
label define labelprempnot
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Employed"
2 "Unemployed"
3 "Not in labor force - discouraged"
4 "Not in labor force - other"
;
label define labelprerelg
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Not eligible for edit"
1 "Eligible for edit"
;
label define labelprexplf
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Employed"
2 "Unemployed"
;
label define labelprfamnum
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Not a family member"
1 "Primary family member only"
2 "Subfamily no. 2 member"
3 "Subfamily no. 3 member"
4 "Subfamily no. 4 member"
5 "Subfamily no. 5 member"
6 "Subfamily no. 6 member"
7 "Subfamily no. 7 member"
8 "Subfamily no. 8 member"
9 "Subfamily no. 9 member"
10 "Subfamily no. 10 member"
11 "Subfamily no. 11 member"
12 "Subfamily no. 12 member"
13 "Subfamily no. 13 member"
14 "Subfamily no. 14 member"
15 "Subfamily no. 15 member"
16 "Subfamily no. 16 member"
17 "Subfamily no. 17 member"
18 "Subfamily no. 18 member"
19 "Subfamily no. 19 member"
;
label define labelprfamrel
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Not a family member"
1 "Reference person"
2 "Spouse"
3 "Child"
4 "Other relative (primary family only)"
;
label define labelprfamtyp
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Primary family"
2 "Primary individual"
3 "Related subfamily"
4 "Unrelated subfamily"
5 "Secondary individual"
;
label define labelprftlf
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Full time labor force"
2 "Part time labor force"
;
label define labelprhernal
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "PRERNHLY does not contain allocated information"
1 "PRERNHLY contains allocated information"
;
label define labelprhrusl
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "0-20 hours"
2 "21-34 hours"
3 "35-39 hours"
4 "40 hours"
5 "41-49 hours"
6 "50 or more hours"
7 "Varies - full time"
8 "Varies - part time"
;
label define labelprimind1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Agriculture, forestry, fishing, and hunting"
2 "Mining"
3 "Construction"
4 "Manufacturing - durable goods"
5 "Manufacturing - non-durable goods"
6 "Wholesale trade"
7 "Retail trade"
8 "Transportation and warehousing"
9 "Utilities"
10 "Information"
11 "Finance and insurance"
12 "Real estate and rental and leasing"
13 "Professional and technical services"
14 "Management, administrative and waste management services"
15 "Educational services"
16 "Health care and social services"
17 "Arts, entertainment, and recreation"
18 "Accommodation and food services"
19 "Private households"
20 "Other services, except private households"
21 "Public administration"
22 "Armed Forces"
;
label define labelprimind2
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Agriculture, forestry, fishing, and hunting"
2 "Mining"
3 "Construction"
4 "Manufacturing - durable goods"
5 "Manufacturing - non-durable goods"
6 "Wholesale trade"
7 "Retail trade"
8 "Transportation and warehousing"
9 "Utilities"
10 "Information"
11 "Finance and insurance"
12 "Real estate and rental and leasing"
13 "Professional and technical services"
14 "Management, administrative and waste management services"
15 "Educational services"
16 "Health care and social services"
17 "Arts, entertainment, and recreation"
18 "Accommodation and food services"
19 "Private households"
20 "Other services, except private households"
21 "Public administration"
22 "Armed Forces"
;
label define labelprinuyer
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Not foreign born"
1 "Before 1950"
2 "1950-1959"
3 "1960-1964"
4 "1965-1969"
5 "1970-1974"
6 "1975-1979"
7 "1980-1981"
8 "1982-1983"
9 "1984-1985"
10 "1986-1987"
11 "1988-1989"
12 "1990-1991"
13 "1992-1993"
14 "1994-1995"
15 "1996-1997"
16 "1998-1999"
17 "2000-2001 or 2000-2002 or 2000-2003 (see note)"
18 "2002-2003 or 2002-2004 or 2002-2005 (see note)"
19 "2004-2005 or 2004-2006 or 2004-2007 (see note)"
20 "2006-2007 or 2006-2008 or 2006-2009 (see note)"
21 "2008-2009 or 2008-2010 or 2008-2011 (see note)"
22 "2010-2011 or 2010-2012 or 2010-2013 (see note)"
23 "2012-2013 or 2012-2014 or 2012-2015 (see note)"
24 "2014-2015 or 2014-2016 or 2014-2017 (see note)"
25 "2016-2017 or 2016-2018 or 2016-2019 (see note)"
26 "2018-2019 or 2018-2020 or 2018-2021 (see note)"
27 "2020-2021 or 2020-2022 or 2020-2023 (see note)"
28 "2022-2024 (see note)"
;
label define labelprioelg
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Not eligible for edit"
1 "Eligible for edit"
;
label define labelprjobsea
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Looked last 4 weeks - not worked"
2 "Looked last 4 weeks - worked"
3 "Looked last 4 weeks - layoff"
4 "Unavailable job seekers"
5 "No recent job search"
;
label define labelprmarsta
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Married, civilian spouse present"
2 "Married, Armed Forces spouse present"
3 "Married, spouse absent (except separated)"
4 "Widowed"
5 "Divorced"
6 "Separated"
7 "Never married"
;
label define labelprmjind1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Agriculture, forestry, fishing, and hunting"
2 "Mining"
3 "Construction"
4 "Manufacturing"
5 "Wholesale and retail trade"
6 "Transportation and utilities"
7 "Information"
8 "Financial activities"
9 "Professional and business services"
10 "Educational and health services"
11 "Leisure and hospitality"
12 "Other services"
13 "Public administration"
14 "Armed Forces"
;
label define labelprmjind2
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Agriculture, forestry, fishing, and hunting"
2 "Mining"
3 "Construction"
4 "Manufacturing"
5 "Wholesale and retail trade"
6 "Transportation and utilities"
7 "Information"
8 "Financial activities"
9 "Professional and business services"
10 "Educational and health services"
11 "Leisure and hospitality"
12 "Other services"
13 "Public administration"
14 "Armed Forces"
;
label define labelprmjocc1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Management, business, and financial occupations"
2 "Professional and related occupations"
3 "Service occupations"
4 "Sales and related occupations"
5 "Office and administrative support occupations"
6 "Farming, fishing, and forestry occupations"
7 "Construction and extraction occupations"
8 "Installation, maintenance, and repair occupations"
9 "Production occupations"
10 "Transportation and material moving occupations"
11 "Armed Forces"
;
label define labelprmjocc2
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Management, business, and financial occupations"
2 "Professional and related occupations"
3 "Service occupations"
4 "Sales and related occupations"
5 "Office and administrative support occupations"
6 "Farming, fishing, and forestry occupations"
7 "Construction and extraction occupations"
8 "Installation, maintenance, and repair occupations"
9 "Production occupations"
10 "Transportation and material moving occupations"
11 "Armed Forces"
;
label define labelprmjocgr
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Management, professional, and related occupations"
2 "Service occupations"
3 "Sales and office occupations"
4 "Farming, fishing, and forestry occupations"
5 "Construction and maintenance occupations"
6 "Production, transportation, and material moving occupations"
7 "Armed Forces"
;
label define labelprnagpws
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Non-agricultural private wage and salary"
;
label define labelprnagws
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Non-agricultural wage and salary workers"
;
label define labelprnlfsch
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "In school"
2 "Not in school"
;
label define labelprnmchld
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
13 "13 Own Child Under 18 Years Of Age"
14 "14 Own Child Under 18 Years Of Age"
15 "15 Own Child Under 18 Years Of Age"
16 "16 Own Child Under 18 Years Of Age"
17 "17 Own Child Under 18 Years Of Age"
18 "18 Own Child Under 18 Years Of Age"
19 "19 Own Child Under 18 Years Of Age"
;
label define labelprpertyp
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Child household member"
2 "Adult civilian household member (15+ years old)"
3 "Adult Armed Forces household member"
;
label define labelprpthrs
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Usually full time, part time for non-economic reasons"
1 "Usually full time, part time for economic reasons, 1-4 hours"
2 "Usually full time, part time for economic reasons, 5-14 hours"
3 "Usually full time, part time for economic reasons, 15-29 hours"
4 "Usually full time, part time for economic reasons, 30-34 hours"
5 "Usually part time for economic reasons, 1-4 hours"
6 "Usually part time for economic reasons, 5-14 hours"
7 "Usually part time for economic reasons, 15-29 hours"
8 "Usually part time for economic reasons, 30-34 hours"
9 "Usually part time for non-economic reasons, 1-4 hours"
10 "Usually part time for non-economic reasons, 5-14 hours"
11 "Usually part time for non-economic reasons, 15-29 hours"
12 "Usually part time for non-economic reasons, 30-34 hours"
;
label define labelprptrea
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Usually full time - slack work/business conditions"
2 "Usually full time - seasonal work"
3 "Usually full time - job started/ended during week"
4 "Usually full time - vacation/personal day"
5 "Usually full time - own illness/injury/medical appointment"
6 "Usually full time - holiday (religious or legal)"
7 "Usually full time - childcare problems"
8 "Usually full time - other family/personal obligation"
9 "Usually full time - labor dispute"
10 "Usually full time - weather affected job"
11 "Usually full time - school/training"
12 "Usually full time - civic/military duty"
13 "Usually full time - other reason"
14 "Usually part time - slack work/business conditions"
15 "Usually part time - could only find part time work"
16 "Usually part time - seasonal work"
17 "Usually part time - childcare problems"
18 "Usually part time - other family/personal obligation"
19 "Usually part time - health/medical limitations"
20 "Usually part time - school/training"
21 "Usually part time - retired/Social Security limit on earnings"
22 "Usually part time - work week less than 35 hours"
23 "Usually part time - other reason"
;
label define labelprsjmj
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Single jobholder"
2 "Multiple jobholder"
;
label define labelpruntype
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Job loser/on layoff"
2 "Other job loser"
3 "Temporary job ended"
4 "Job leaver"
5 "Re-entrant"
6 "New entrant"
;
label define labelprwernal
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "PRERNWA does not contain allocated information"
1 "PRERNWA contains allocated information"
;
label define labelprwksch
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Not in labor force"
1 "At work"
2 "With job, not at work"
3 "Unemployed, seeks full time"
4 "Unemployed, seeks part time"
;
label define labelprwkstat
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Not in labor force"
2 "Full time hours (35+), usually full time"
3 "Part time for economic reasons, usually full time"
4 "Part time for non-economic reasons, usually full time"
5 "Not at work, usually full time"
6 "Part time hours, usually part time for economic reasons"
7 "Part time hours, usually part time for non-economic reasons"
8 "Full time hours, usually part time for economic reasons"
9 "Full time hours, usually part time for non-economic reasons"
10 "Not at work, usually part time"
11 "Unemployed full time"
12 "Unemployed part time"
;
label define labelprwntjob
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Want a job"
2 "Other not in labor force"
;
label define labelptdtrace
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "White only"
2 "Black only"
3 "American Indian, Alaskan Native only"
4 "Asian only"
5 "Hawaiian/Pacific Islander only"
6 "White-Black"
7 "White-American Indian"
8 "White-Asian"
9 "White-Hawaiian"
10 "Black-American Indian"
11 "Black-Asian"
12 "Black-Hawaiian"
13 "American Indian-Asian"
14 "Asian-Hawaiian or American Indian-Hawaiian (beginning 5/2012)"
15 "White-Black-American Indian or Asian-Hawaiian (beginning 5/2012)"
16 "White-Black-Asian or White-Black-American Indian (beginning 5/2012)"
17 "White-American Indian-Asian or White-Black-Asian (beginning 5/2012)"
18 "White-Asian-Hawaiian or White-Black-Hawaiian (beginning 5/2012)"
19 "White-Black-American Indian-Asian or White-American Indian-Asian (beginning 5/2012)"
20 "2 or 3 races or White-American Indian-Hawaiian (beginning 5/2012)"
21 "4 or 5 races or White-Asian-Hawaiian (beginning 5/2012)"
22 "Black-American Indian-Asian (beginning 5/2012)"
23 "White-Black-American Indian-Asian (beginning 5/2012)"
24 "White-American Indian-Asian-Hawaiian (beginning 5/2012)"
25 "Other 3 race combinations (beginning 5/2012)"
26 "Other 4 and 5 race combinations (beginning 5/2012)"
;
label define labelpthr
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Not topcoded"
1 "Topcoded"
;
label define labelptot
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Not topcoded"
1 "Topcoded"
;
label define labelptwk
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Not topcoded"
1 "Topcoded"
;
label define labelpuabsot
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
3 "Retired"
4 "Disabled"
5 "Unable to work"
;
label define labelpuafever
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpubus1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpubus2ot
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpudis
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
3 "Did not have disability last month"
;
label define labelpudis1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpudis2
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpuhroff1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpuhrot1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpujhdp1o
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpulay
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
3 "Retired"
4 "Disabled"
5 "Unable to work"
;
label define labelpulay6m
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpulayavr
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Own temporary illness"
2 "Going to school"
3 "Other"
;
label define labelpulaydt
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpulk
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
3 "Retired"
4 "Disabled"
5 "Unable to work"
;
label define labelpulkavr
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Waiting for new job to begin"
2 "Own temporary illness"
3 "Going to school"
4 "Other"
;
label define labelpulkdk1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Contacted employer directly/interview"
2 "Contacted public employment agency"
3 "Contacted private employment agency"
4 "Contacted friends or relatives"
5 "Contacted school/university employment center"
6 "Sent out resumes/filled out applications"
7 "Checked union/professional registers"
8 "Placed or answered ads"
9 "Other active"
10 "Looked at ads"
11 "Attended job training programs/courses"
12 "Nothing"
13 "Other passive"
;
label define labelpulkdk2
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Contacted employer directly/interview"
2 "Contacted public employment agency"
3 "Contacted private employment agency"
4 "Contacted friends or relatives"
5 "Contacted school/university employment center"
6 "Sent out resumes/filled out applications"
7 "Checked union/professional registers"
8 "Placed or answered ads"
9 "Other active"
10 "Looked at ads"
11 "Attended job training programs/courses"
13 "Other passive"
;
label define labelpulkdk3
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Contacted employer directly/interview"
2 "Contacted public employment agency"
3 "Contacted private employment agency"
4 "Contacted friends or relatives"
5 "Contacted school/university employment center"
6 "Sent out resumes/filled out applications"
7 "Checked union/professional registers"
8 "Placed or answered ads"
9 "Other active"
10 "Looked at ads"
11 "Attended job training programs/courses"
13 "Other passive"
;
label define labelpulkdk4
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Contacted Employer Directly/Interview"
2 "Contacted Public Employment Agency"
3 "Contacted Private Employment Agency"
4 "Contacted Friends Or Relatives"
5 "Contacted School/University Empl Center"
6 "Sent Out Resumes/Filled Out Application"
7 "Checked Union/Professional Registers"
8 "Placed Or Answered Ads"
9 "Other Active"
10 "Looked At Ads"
11 "Attended Job Training Programs/Courses"
13 "Other Passive"
;
label define labelpulkm2
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Contacted employer directly/interview"
2 "Contacted public employment agency"
3 "Contacted private employment agency"
4 "Contacted friends or relatives"
5 "Contacted school/university employment center"
6 "Sent out resumes/filled out applications"
7 "Checked union/professional registers"
8 "Placed or answered ads"
9 "Other active"
10 "Looked at ads"
11 "Attended job training programs/courses"
13 "Other passive"
;
label define labelpulkm3
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Contacted Employer Directly/Interview"
2 "Contacted Public Employment Agency"
3 "Contacted Private Employment Agency"
4 "Contacted Friends Or Relatives"
5 "Contacted School/University Empl Center"
6 "Sent Out Resumes/Filled Out Application"
7 "Checked Union/Professional Registers"
8 "Placed Or Answered Ads"
9 "Other Active"
10 "Looked At Ads"
11 "Attended Job Training Programs/Courses"
13 "Other Passive"
;
label define labelpulkm4
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Contacted Employer Directly/Interview"
2 "Contacted Public Employment Agency"
3 "Contacted Private Employment Agency"
4 "Contacted Friends Or Relatives"
5 "Contacted School/University Empl Center"
6 "Sent Out Resumes/Filled Out Application"
7 "Checked Union/Professional Registers"
8 "Placed Or Answered Ads"
9 "Other Active"
10 "Looked At Ads"
11 "Attended Job Training Programs/Courses"
13 "Other Passive"
;
label define labelpulkm5
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Contacted Employer Directly/Interview"
2 "Contacted Public Employment Agency"
3 "Contacted Private Employment Agency"
4 "Contacted Friends Or Relatives"
5 "Contacted School/University Empl Center"
6 "Sent Out Resumes/Filled Out Application"
7 "Checked Union/Professional Registers"
8 "Placed Or Answered Ads"
9 "Other Active"
10 "Looked At Ads"
11 "Attended Job Training Programs/Courses"
13 "Other Passive"
;
label define labelpulkm6
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Contacted Employer Directly/Interview"
2 "Contacted Public Employment Agency"
3 "Contacted Private Employment Agency"
4 "Contacted Friends Or Relatives"
5 "Contacted School/University Empl Center"
6 "Sent Out Resumes/Filled Out Application"
7 "Checked Union/Professional Registers"
8 "Placed Or Answered Ads"
9 "Other Active"
10 "Looked At Ads"
11 "Attended Job Training Programs/Courses"
13 "Other Passive"
;
label define labelpulkps1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Contacted employer directly/interview"
2 "Contacted public employment agency"
3 "Contacted private employment agency"
4 "Contacted friends or relatives"
5 "Contacted school/university employment center"
6 "Sent out resumes/filled out applications"
7 "Checked union/professional registers"
8 "Placed or answered ads"
9 "Other active"
10 "Looked at ads"
11 "Attended job training programs/courses"
12 "Nothing"
13 "Other passive"
;
label define labelpulkps2
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Contacted employer directly/interview"
2 "Contacted public employment agency"
3 "Contacted private employment agency"
4 "Contacted friends or relatives"
5 "Contacted school/university employment center"
6 "Sent out resumes/filled out applications"
7 "Checked union/professional registers"
8 "Placed or answered ads"
9 "Other active"
10 "Looked at ads"
11 "Attended job training programs/courses"
13 "Other passive"
;
label define labelpulkps3
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Contacted Employer Directly/Interview"
2 "Contacted Public Employment Agency"
3 "Contacted Private Employment Agency"
4 "Contacted Friends Or Relatives"
5 "Contacted School/University Empl Center"
6 "Sent Out Resumes/Filled Out Application"
7 "Checked Union/Professional Registers"
8 "Placed Or Answered Ads"
9 "Other Active"
10 "Looked At Ads"
11 "Attended Job Training Programs/Courses"
13 "Other Passive"
;
label define labelpulkps4
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Contacted Employer Directly/Interview"
2 "Contacted Public Employment Agency"
3 "Contacted Private Employment Agency"
4 "Contacted Friends Or Relatives"
5 "Contacted School/University Empl Center"
6 "Sent Out Resumes/Filled Out Application"
7 "Checked Union/Professional Registers"
8 "Placed Or Answered Ads"
9 "Other Active"
10 "Looked At Ads"
11 "Attended Job Training Programs/Courses"
13 "Other Passive"
;
label define labelpupelig
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Eligible for interview"
2 "Labor force fully complete"
3 "Missing labor force data for person"
4 "(Not used)"
5 "Assigned if PUAGERNG 0"
6 "Armed Forces member"
7 "Under 15 years old"
8 "Not a household member"
9 "Deleted"
10 "Deceased"
11 "End of list"
12 "After end of list"
;
label define labelpuretot
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
3 "Was not retired last month"
;
label define labelpuslfprx
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Self"
2 "Proxy"
3 "Both self and proxy"
;
label define labelpuwk
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
3 "Retired"
4 "Disabled"
5 "Unable to work"
;
label define labeltratusr
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Did not respond to ATUS"
1 "Responded to ATUS"
;
label define labelptcovid1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelptcovid2
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelptcovid3
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelptcovid4
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelptcovid5w
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpepar1typ
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Biological"
2 "Step"
3 "Adopted"
;
label define labelpepar2typ
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Biological"
2 "Step"
3 "Adopted"
;
label define labelprernmin
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Minimum wage flag"
;
label define labelptcovr1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelptcovr2
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
;
label define labelptcovr3
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelptcovr4
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "More"
2 "Less"
3 "About the same"
;
label define labelpxcovr1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "PTCOVR1 does not contain allocated information"
1 "PTCOVR1 contains allocated information"
;
label define labelpxcovr2
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "PTCOVR2 does not contain allocated information"
1 "PTCOVR2 contains allocated information"
;
label define labelpxcovr3
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "PTCOVR3 does not contain allocated information"
1 "PTCOVR3 contains allocated information"
;
label define labelpxcovr4
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "PTCOVR4 does not contain allocated information"
1 "PTCOVR4 contains allocated information"
;
label define labelpttlwk
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelpxtlwk
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "PTTLWK does not contain allocated information"
1 "PTTLWK contains allocated information"
;
label define labelpxtlwkhr
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "PTTLWKHR does not contain allocated information"
1 "PTTLWKHR contains allocated information"
;


label values gediv labelgediv;
label values gereg labelgereg;
label values gemetsta labelgemetsta;
label values gtmetsta labelgtmetsta;
label values hefaminc labelhefaminc;
label values hehousut labelhehousut;
label values hephoneo labelhephoneo;
label values hetelavl labelhetelavl;
label values hetelhhd labelhetelhhd;
label values hetenure labelhetenure;
label values hrhtype labelhrhtype;
label values hrintsta labelhrintsta;
label values hrlonglk labelhrlonglk;
label values hrmis labelhrmis;
label values hubus labelhubus;
label values hufaminc labelhufaminc;
label values hufinal labelhufinal;
label values huinttyp labelhuinttyp;
label values huspnish labelhuspnish;
label values hxfaminc labelhxfaminc;
label values peabspdo labelpeabspdo;
label values peabsrsn labelpeabsrsn;
label values peafever labelpeafever;
label values peafnow labelpeafnow;
label values peafwhen labelpeafwhen;
label values peafwhn1 labelpeafwhn1;
label values peafwhn2 labelpeafwhn2;
label values peafwhn3 labelpeafwhn3;
label values peafwhn4 labelpeafwhn4;
label values pecert1 labelpecert1;
label values pecert2 labelpecert2;
label values pecert3 labelpecert3;
label values pecyc labelpecyc;
label values pedadtyp   labelpedadtyp;
label values pedipged labelpedipged;
label values pedisdrs labelpedisdrs;
label values pedisear labelpedisear;
label values pediseye labelpediseye;
label values pedisout labelpedisout;
label values pedisphy labelpedisphy;
label values pedisrem labelpedisrem;
label values pedw4wk labelpedw4wk;
label values pedwavl labelpedwavl;
label values pedwavr labelpedwavr;
label values pedwlko labelpedwlko;
label values pedwlkwk labelpedwlkwk;
label values pedwrsn labelpedwrsn;
label values pedwwk labelpedwwk;
label values pedwwnto labelpedwwnto;
label values peeduca labelpeeduca;
label values peerncov labelpeerncov;
label values peernhry labelpeernhry;
label values peernlab labelpeernlab;
label values peernper labelpeernper;
label values peernrt labelpeernrt;
label values peernuot labelpeernuot;
label values pegr6cor labelpegr6cor;
label values pegrprof labelpegrprof;
label values pehgcomp labelpehgcomp;
label values pehravl labelpehravl;
label values pehrftpt labelpehrftpt;
label values pehrrsn1 labelpehrrsn1;
label values pehrrsn2 labelpehrrsn2;
label values pehrrsn3 labelpehrrsn3;
label values pehrwant labelpehrwant;
label values pehspnon labelpehspnon;
label values peio1cow labelpeio1cow;
label values peio2cow labelpeio2cow;
label values pejhrsn labelpejhrsn;
label values pejhwant labelpejhwant;
label values pejhwko labelpejhwko;
label values pelayavl labelpelayavl;
label values pelayfto labelpelayfto;
label values pelaylk labelpelaylk;
label values pelkavl labelpelkavl;
label values pelkfto labelpelkfto;
label values pelkll1o labelpelkll1o;
label values pelkll2o labelpelkll2o;
label values pelklwo labelpelklwo;
label values pelkm1 labelpelkm1;
label values pemaritl labelpemaritl;
label values pemjnum labelpemjnum;
label values pemjot labelpemjot;
label values pemlr labelpemlr;
label values pems123 labelpems123;
label values penlfact labelpenlfact;
label values penlfjh labelpenlfjh;
label values penlfret labelpenlfret;
label values pepdemp1 labelpepdemp1;
label values pepdemp2 labelpepdemp2;
label values peret1 labelperet1;
label values perrp labelperrp;
label values peschenr labelpeschenr;
label values peschft labelpeschft;
label values peschlvl labelpeschlvl;
label values pesex labelpesex;
label values prabsrea labelprabsrea;
label values pragna labelpragna;
label values prcitshp labelprcitshp;
label values prcivlf labelprcivlf;
label values prcow1 labelprcow1;
label values prcow2 labelprcow2;
label values prcowpg labelprcowpg;
label values prdasian labelprdasian;
label values prdisc labelprdisc;
label values prdisflg labelprdisflg;
label values prdtcow1 labelprdtcow1;
label values prdtcow2 labelprdtcow2;
label values prdthsp labelprdthsp;
label values prdtind1 labelprdtind1;
label values prdtind2 labelprdtind2;
label values prdtocc1 labelprdtocc1;
label values prdtocc2 labelprdtocc2;
label values premp labelpremp;
label values premphrs labelpremphrs;
label values prempnot labelprempnot;
label values prerelg labelprerelg;
label values prexplf labelprexplf;
label values prfamnum labelprfamnum;
label values prfamrel labelprfamrel;
label values prfamtyp labelprfamtyp;
label values prftlf labelprftlf;
label values prhernal labelprhernal;
label values prhrusl labelprhrusl;
label values primind1 labelprimind1;
label values primind2 labelprimind2;
label values prinuyer labelprinuyer;
label values prioelg labelprioelg;
label values prjobsea labelprjobsea;
label values prmarsta labelprmarsta;
label values prmjind1 labelprmjind1;
label values prmjind2 labelprmjind2;
label values prmjocc1 labelprmjocc1;
label values prmjocc2 labelprmjocc2;
label values prmjocgr labelprmjocgr;
label values prnagpws labelprnagpws;
label values prnagws labelprnagws;
label values prnlfsch labelprnlfsch;
label values prnmchld labelprnmchld;
label values prpertyp labelprpertyp;
label values prpthrs labelprpthrs;
label values prptrea labelprptrea;
label values prsjmj labelprsjmj;
label values pruntype labelpruntype;
label values prwernal labelprwernal;
label values prwksch labelprwksch;
label values prwkstat labelprwkstat;
label values prwntjob labelprwntjob;
label values ptdtrace labelptdtrace;
label values pthr labelpthr;
label values ptot labelptot;
label values ptwk labelptwk;
label values puabsot labelpuabsot;
label values puafever labelpuafever;
label values pubus1 labelpubus1;
label values pubus2ot labelpubus2ot;
label values pudis labelpudis;
label values pudis1 labelpudis1;
label values pudis2 labelpudis2;
label values puhroff1 labelpuhroff1;
label values puhrot1 labelpuhrot1;
label values pujhdp1o labelpujhdp1o;
label values pulay labelpulay;
label values pulay6m labelpulay6m;
label values pulayavr labelpulayavr;
label values pulaydt labelpulaydt;
label values pulk labelpulk;
label values pulkavr labelpulkavr;
label values pulkdk1 labelpulkdk1;
label values pulkdk2 labelpulkdk2;
label values pulkdk3 labelpulkdk3;
label values pulkdk4 labelpulkdk4;
label values pulkm2 labelpulkm2;
label values pulkm3 labelpulkm3;
label values pulkm4 labelpulkm4;
label values pulkm5 labelpulkm5;
label values pulkm6 labelpulkm6;
label values pulkps1 labelpulkps1;
label values pulkps2 labelpulkps2;
label values pulkps3 labelpulkps3;
label values pulkps4 labelpulkps4;
label values pupelig labelpupelig;
label values puretot labelpuretot;
label values puslfprx labelpuslfprx;
label values puwk labelpuwk;
label values tratusr labeltratusr;
label values ptcovid1 labelptcovid1;
label values ptcovid2 labelptcovid2;
label values ptcovid3 labelptcovid3;
label values ptcovid4 labelptcovid4;
label values ptcovid5w labelptcovid5w;
label values pepar1typ labelpepar1typ;
label values pepar2typ labelpepar2typ;
/*label values pefntvty   labelpefntvty;*/
/*label values pemntvty   labelpemntvty;*/
/*label values penatvty   labelpenatvty;*/
label values prernmin labelprernmin;
label values ptcovr1  labelptcovr1;
label values ptcovr2  labelptcovr2;
label values ptcovr3  labelptcovr3;
label values ptcovr4  labelptcovr4;
label values pxcovr1  labelpxcovr1;
label values pxcovr2  labelpxcovr2;
label values pxcovr3  labelpxcovr3;
label values pxcovr4  labelpxcovr4;
label values pttlwk labelpttlwk;
label values pxtlwk labelpxtlwk;
label values pxtlwkhr labelpxtlwkhr;
describe, short;
