#delimit ;
 
* Edit the import statement to reference the data file on your computer.;
 
import delimited
tucaseid
tulineno
tespuhrs
trdtind1
trdtocc1
trernhly
trernupd
trhernal
trhhchild
trimind1
trmjind1
trmjocc1
trmjocgr
trnhhchild
trnumhou
trohhchild
trtalone
trtcc
trthhfamily
trtnochild
trtnohh
trto
trtohh
trtohhchild
trtonhh
trtonhhchild
trtsponly
trtspouse
trtunmpart
trwernal
tthr
ttot
ttwk
tuabsot
tuyear 
teabsrsn
teern
teernh1o
teernh2
teernhro
teernhry
teernper
teernrt
teernuot
teernwkp
tehrftpt
tehrusl1 
tehrusl2 
teio1cow
teio1icd 
teio1ocd 
telayavl
telaylk
telkavl
telkm1
teret1
teschft
tubus
tubus1
tubus2ot
tubusl1
tubusl2
tubusl3
tubusl4
tucc2 
tucc4 
tufwk
tuio1mfg
tuiodp1
tuiodp2
tuiodp3
tulay
tulay6m
tulayavr
tulaydt
tulk
tulkavr
tulkdk1
tulkdk2
tulkdk3
tulkdk4
tulkm2
tulkm3
tulkm4
tulkm5
tulkm6
tulkps1
tulkps2
tulkps3
tulkps4
tumonth
trtccc
trtcctot
trtchild
trtcoc
trtfamily
trtfriend
trthh
tudis2
turetot
tuspabs
tuspusft
tuspwk
tremodr
tucc9
tudiarydate 
tudis
tudis1
trchildnum
tudiaryday
trernwa
trholiday
trspftpt
trsppres
trdpftpt
tufnwgtp
tespempnot
teschlvl
teschenr
temjot
telfs
tehruslt 
tryhhchild
trwbmodr
trtalone_wk
trtccc_wk
trlvmodr
trtec
tuecytd
tuelder
tuelfreq
tuelnum
tu20fwgt
 using c:\atusresp_0324.dat, stringcols(1) ;
 
label variable teabsrsn "Edited: what was the main reason you were absent from your job last week?";
label variable teern "Edited: total weekly overtime earnings (2 implied decimals)";
label variable teernh1o "Edited: hrly pay rate (main job) exc. overtime, tips, & commissions (2 decimals)";
label variable teernh2 "Edited: hrly pay rate (main job) exc. overtime, tips, & commissions (2 decimals)";
label variable teernhro "Edited: how many hours do you usually work per week at this rate?";
label variable teernhry "Edited: hourly/non-hourly status";
label variable teernper "Edited: main job, easiest to report earnings: hourly, weekly, annually, or other";
label variable teernrt "Edited:  are you paid at an hourly rate on this job?";
label variable teernuot "Edited: usually receive overtime pay, tips, or commissions at your main job?";
label variable teernwkp "Edited: how many weeks a year do you get paid?";
label variable tehrftpt "Edited: do you usually work > 35 hours per week at your job(s)/family business?";
label variable tehrusl1 "Edited: how many hours per week do you usually work at your main job?";
label variable tehrusl2 "Edited: how many hours per week do you usually work at your other job(s)?";
label variable tehruslt "Edited: total hours usually worked per week (sum of TEHRUSL1 and TEHRUSL2)";
label variable teio1cow "Edited: individual class of worker code (main job)";
label variable teio1icd "Edited: industry code (main job)";
label variable teio1ocd "Edited: occupation code (main job)";
label variable telayavl "Edited: could you have returned to work in the last 7 days if recalled?";
label variable telaylk "Edited: have you been looking for work during the last 4 weeks? (Laid off)";
label variable telfs "Edited: labor force status";
label variable telkavl "Edited: could you have started a job in the last 7 days if one had been offered?";
label variable telkm1 "Edited: things you have done to find work during the last 4 weeks? (1st method)";
label variable temjot "Edited: in the last 7 days did you have more than one job?";
label variable teret1 "Edited: do you currently want a job, either full or part time?";
label variable teschenr "Edited: are you enrolled in high school, college, or university?";
label variable teschft "Edited: are you enrolled as a full-time or part-time student?";
label variable teschlvl "Edited: would that be high school, college, or university?";
label variable tespempnot "Edited: employment status of spouse or unmarried partner";
label variable tespuhrs "Edited: usual hours of work of spouse or unmarried partner";
label variable trchildnum "Number of household children < 18";
label variable trdpftpt "Full time or part time employment status of respondent";
label variable trdtind1 "Detailed industry recode (main job)";
label variable trdtocc1 "Detailed occupation recode (main job)";
label variable tremodr "Eating and Health Module respondent";
label variable trernhly "Hourly earnings (2 implied decimals)";
label variable trernupd "Earnings update flag";
label variable trernwa "Weekly earnings (2 implied decimals)";
label variable trhernal "TRERNHLY: allocation flag";
label variable trhhchild "Presence of household children < 18";
label variable trholiday "Flag to indicate if diary day was a holiday";
label variable trimind1 "Intermediate industry recode (main job)";
label variable trlvmodr "Leave module respondent";
label variable trmjind1 "Major industry recode (main job)";
label variable trmjocc1 "Major occupation recode (main job)";
label variable trmjocgr "Major occupation category (main job)";
label variable trnhhchild "Presence of own non-household child < 18";
label variable trnumhou "Number of people living in respondent's household";
label variable trohhchild "Presence of own household children < 18";
label variable trspftpt "Full time or part time employment status of spouse or unmarried partner";
label variable trsppres "Presence of the respondent's spouse or unmarried partner in the household";
label variable trtalone "Total time respondent spent alone (in minutes)";
label variable trtalone_wk "Total work- and nonwork-related time respondent spent alone (in minutes)";
label variable trtcc "Minutes diary day providing secondary childcare for hh & own nonhh children < 13";
label variable trtccc "Total time respondent spent with customers, clients, and coworkers (in minutes)";
label variable trtccc_wk "Minutes work- and nonwork-related time with customers/clients/coworkers";
label variable trtcctot "Minutes during diary day providing secondary childcare for all children < 13 ";
label variable trtchild "Minutes respondent spent with household or nonhousehold children < 18";
label variable trtcoc "Minutes diary day providing secondary childcare for nonown, nonhh children < 13";
label variable trtec "Total time spent providing eldercare (in minutes)";
label variable trtfamily "Total time respondent spent with family members (in minutes)";
label variable trtfriend "Total time respondent spent with friends (in minutes)";
label variable trthh "Minutes during diary day providing secondary childcare for hh children < 13";
label variable trthhfamily "Total time respondent spent with household family members (in minutes)";
label variable trtnochild "Total time respondent spent with nonown children < 18 (in minutes)";
label variable trtnohh "Minutes diary day providing secondary childcare for nonown hh children < 13";
label variable trto "Minutes during diary day providing secondary childcare for own children < 13";
label variable trtohh "Minutes diary day providing secondary childcare for own household children < 13 ";
label variable trtohhchild "Total time respondent spent with own household children < 18 (in minutes)";
label variable trtonhh "Minutes diary day providing secondary childcare for own nonhh children < 13";
label variable trtonhhchild "Total time respondent spent with own nonhousehold children < 18 (in minutes)";
label variable trtsponly "Total time respondent spent with spouse only (in minutes)";
label variable trtspouse "Total time respondent spent with spouse (others may be present) (in minutes)";
label variable trtunmpart "Minutes spent with unmarried partner (others may be present)";
label variable trwbmodr "Well-Being Module respondent";
label variable trwernal "TRERNWA: allocation flag";
label variable tryhhchild "Age of youngest household child < 18";
label variable tthr "Hourly pay topcode flag";
label variable ttot "Overtime amount topcode flag";
label variable ttwk "Weekly earnings topcode flag";
label variable tuabsot "In the last 7 days, did you have a job either full or part time?";
label variable tubus "Does anyone in the household own a business or a farm?";
label variable tubus1 "In the last 7 days, did you do any unpaid work in the family business or farm?";
label variable tubus2ot "Do you receive payments or profits from the business?";
label variable tubusl1 "TULINENO of farm or business owner (first owner)";
label variable tubusl2 "TULINENO of farm or business owner (second owner)";
label variable tubusl3 "TULINENO of farm or business owner (third owner)";
label variable tubusl4 "TULINENO of farm or business owner (fourth owner)";
label variable tucaseid "ATUS Case ID (14-digit identifier)";
label variable tucc2 "Time first household child < 13 woke up";
label variable tucc4 "Time last household child < 13 went to bed";
label variable tucc9 "Are the non-own, non-household children you cared for in TUCC8 related to you?";
label variable tudiarydate "Date of diary day (date about which the respondent was interviewed)";
label variable tudiaryday "Day of the week of diary day (day about which the respondent was interviewed)";
label variable tudis "Disability prevent you from doing any kind of work for the next 6 months?";
label variable tudis1 "Disability that prevents you accepting any kind of work during next 6 months?";
label variable tudis2 "Disability that prevents you accepting any kind of work during next 6 months?";
label variable tuecytd "Did you provide any eldercare or assistance yesterday?";
label variable tuelder "Since 1st of [REF_MONTH], cared for adult due to condition related to aging?";
label variable tuelfreq "How often did you provide this care?";
label variable tuelnum "Since the first of [REF_MONTH], how many people have you provided this care to?";
label variable tufnwgtp "ATUS final weight";
label variable tufwk "In the last 7 days did you do any work for pay or profit?";
label variable tuio1mfg "Business/organization mfg., retail trade, wholesale, something else? (main job)";
label variable tuiodp1 "Do you still work for (CPS employer's name)? (main job)";
label variable tuiodp2 "Usual activities and duties of job changed since (CPS interview)? (main job)";
label variable tuiodp3 "Occupation/duties changed since CPS interview? (main job)";
label variable tulay "During the last 7 days were you on layoff from your job?";
label variable tulay6m "Any indication recalled to work within the next 6 months?";
label variable tulayavr "Why could you not have started a job in the last week?";
label variable tulaydt "Has your employer given you a date to return to work? (to layoff job) ";
label variable tulineno "ATUS person line number";
label variable tulk "Have you been doing anything to find work during the last four weeks?";
label variable tulkavr "Why could you not have started a job last week?";
label variable tulkdk1 "Said trying to find work. How did you go about looking? (1st method)";
label variable tulkdk2 "TULKDK1 text: (second method)";
label variable tulkdk3 "TULKDK1 text: (third method)";
label variable tulkdk4 "TULKDK1 text: (fourth method)";
label variable tulkm2 "Things you have done to find work during the last 4 weeks? (second method)";
label variable tulkm3 "TULKM2 text: (third method)";
label variable tulkm4 "TULKM2 text: (fourth method)";
label variable tulkm5 "TULKM2 text: (fifth method)";
label variable tulkm6 "TULKM2 text: (sixth method)";
label variable tulkps1 "Can you tell me more about what you did to search for work? (first method)";
label variable tulkps2 "TULKPS1 text: (second method)";
label variable tulkps3 "TULKPS1 text: (third method)";
label variable tulkps4 "TULKPS1 text: (fourth method)";
label variable tumonth "Month of diary day (month of day about which ATUS respondent was interviewed)";
label variable turetot "Are you still retired? (Retired in CPS)";
label variable tuspabs "In the last 7 days, spouse/unmarried partner have a job either full or part time?";
label variable tuspusft "Does your spouse or unmarried partner usually work 35 hours or more per week?";
label variable tuspwk "In the last 7 days, spouse/unmarried partner do any work for pay or profit?";
label variable tuyear "Year of diary day (year of day about which respondent was interviewed)";
label variable tu20fwgt "ATUS final weight with method used for 2020 pandemic";

label define labelteabsrsn
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "On layoff (temporary or indefinite)"
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
label define labelteernhry
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Paid hourly"
2 "Not paid hourly"
;
label define labelteernper
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
label define labelteernrt
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelteernuot
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labeltehrftpt
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
3 "Hours vary"
;
label define labelteio1cow
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
label define labeltelayavl
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labeltelaylk
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labeltelfs
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Employed - at work"
2 "Employed - absent"
3 "Unemployed - on layoff"
4 "Unemployed - looking"
5 "Not in labor force"
;
label define labeltelkavl
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labeltelkm1
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
label define labeltemjot
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelteret1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes or maybe/it depends"
2 "No"
3 "Has a job"
;
label define labelteschenr
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labelteschft
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Full time"
2 "Part time"
;
label define labelteschlvl
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "High school"
2 "College or university"
;
label define labeltespempnot
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Employed"
2 "Not employed"
;
label define labeltrdpftpt
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Full time"
2 "Part time"
;
label define labeltrdtocc1
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
;
label define labeltremodr
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Did not respond to Eating and Health Module"
1 "Responded to Eating and Health Module"
;
label define labeltrernupd
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Earnings carried forward from final CPS interview"
1 "Earnings updated in ATUS"
;
label define labeltrhernal
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "TRERNHLY does not contain allocated information"
1 "TRERNHLY contains allocated information"
;
label define labeltrhhchild
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labeltrholiday
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Diary day was not a holiday"
1 "Diary day was a holiday"
;
label define labeltrimind1
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
;
label define labeltrlvmodr
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Respondent was eligible for the Leave module, but did not complete it."
1 "Respondent completed the leave module."
;
label define labeltrmjind1
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
;
label define labeltrmjocc1
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
;
label define labeltrmjocgr
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Management, professional, and related occupations"
2 "Service occupations"
3 "Sales and office occupations"
4 "Farming, fishing, and forestry occupations"
5 "Construction and maintenance occupations"
6 "Production, transportation, and material moving occupations"
;
label define labeltrnhhchild
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labeltrohhchild
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labeltrspftpt
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Full time"
2 "Part time"
3 "Hours vary"
;
label define labeltrsppres
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Spouse present"
2 "Unmarried partner present"
3 "No spouse or unmarried partner present"
;
label define trwbmodr
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Did not respond to Well-Being Module"
1 "Responded to the Well-Being Module"
;
label define labeltrwernal
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "TRERNWA does not contain allocated information"
1 "TRERNWA contains allocated information"
;
label define labeltthr
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Not topcoded"
1 "Topcoded"
;
label define labelttot
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Not topcoded"
1 "Topcoded"
;
label define labelttwk
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
0 "Not topcoded"
1 "Topcoded"
;
label define labeltuabsot
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
3 "Retired"
4 "Disabled"
5 "Unable to work"
;
label define labeltubus
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labeltubus1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labeltubus2ot
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labeltudiaryday
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Sunday"
2 "Monday"
3 "Tuesday"
4 "Wednesday"
5 "Thursday"
6 "Friday"
7 "Saturday"
;
label define labeltudis
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
3 "Did not have a disability last time"
;
label define labeltudis1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labeltudis2
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labeltuecytd
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labeltuelder
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labeltuelfreq
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Daily"
2 "Several times a week"
3 "About once a week"
4 "Several times a month"
5 "Once a month"
6 "One time"
7 "Other"
;
label define labeltufwk
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
3 "Retired"
4 "Disabled"
5 "Unable to work"
;
label define labeltuio1mfg
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Manufacturing"
2 "Retail trade"
3 "Wholesale trade"
4 "Something else"
;
label define labeltuiodp1
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labeltuiodp2
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labeltuiodp3
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labeltulay
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
3 "Retired"
4 "Disabled"
5 "Unable to work"
;
label define labeltulay6m
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labeltulayavr
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Own temporary illness"
2 "Going to school"
3 "Other"
;
label define labeltulaydt
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
;
label define labeltulk
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
3 "Retired"
4 "Disabled"
5 "Unable to work"
;
label define labeltulkavr
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Waiting for new job to begin"
2 "Own temporary illness"
3 "Going to school"
4 "Other"
;
label define labeltulkdk1
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
label define labeltulkdk2
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
97 "No additional job search activities"
;
label define labeltulkdk3
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Contacted Employer Directly/Interview"
2 "Contacted Public Employment Agency"
3 "Contacted Private Employment Agency"
4 "Contacted Friends or Relatives"
5 "Contacted School/University Employment Center"
6 "Sent Out Resumes/Filled Out Applications"
7 "Check Union/Professional Registers"
8 "Placed or Answered Ads"
9 "Other Active"
10 "Looked at Ads"
11 "Attended Job Training Programs/Courses"
13 "Other Passive"
97 "No Additional Job Search Activities"
;
label define labeltulkdk4
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Contacted Employer Directly/Interview"
2 "Contacted Public Employment Agency"
3 "Contacted Private Employment Agency"
4 "Contacted Friends or Relatives"
5 "Contacted School/University Employment Center"
6 "Sent Out Resumes/Filled Out Applications"
7 "Check Union/Professional Registers"
8 "Placed or Answered Ads"
9 "Other Active"
10 "Looked at Ads"
11 "Attended Job Training Programs/Courses"
13 "Other Passive"
97 "No Additional Job Search Activities"
;
label define labeltulkm2
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
97 "No additional job search activities"
;
label define labeltulkm3
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Contacted employer directly/interview"
2 "Contacted public employment agency"
3 "Contacted private employment agency"
4 "Contacted friends or relatives"
5 "Contacted school/university employment center"
6 "Sent out resumes/filled out applications"
7 "Check union/professional registers"
8 "Placed or answered ads"
9 "Other active"
10 "Looked at ads"
11 "Attended job training programs/courses"
13 "Other passive"
97 "No additional job search activities"
;
label define labeltulkm4
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Contacted employer directly/interview"
2 "Contacted public employment agency"
3 "Contacted private employment agency"
4 "Contacted friends or relatives"
5 "Contacted school/university employment center"
6 "Sent out resumes/filled out applications"
7 "Check union/professional registers"
8 "Placed or answered ads"
9 "Other active"
10 "Looked at ads"
11 "Attended job training programs/courses"
13 "Other passive"
97 "No additional job search activities"
;
label define labeltulkps1
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
97 "No more job search activities"
;
label define labeltulkps2
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
97 "No additional job search activities"
;
label define labeltulkps3
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Contacted Employer Directly/Interview"
2 "Contacted Public Employment Agency"
3 "Contacted Private Employment Agency"
4 "Contacted Friends or Relatives"
5 "Contacted School/University Employment Center"
6 "Sent Out Resumes/Filled Out Applications"
7 "Check Union/Professional Registers"
8 "Placed or Answered Ads"
9 "Other Active"
10 "Looked at Ads"
11 "Attended Job Training Programs/Courses"
13 "Other Passive"
97 "No Additional Job Search Activities"
;
label define labeltulkps4
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Contacted Employer Directly/Interview"
2 "Contacted Public Employment Agency"
3 "Contacted Private Employment Agency"
4 "Contacted Friends or Relatives"
5 "Contacted School/University Employment Center"
6 "Sent Out Resumes/Filled Out Applications"
7 "Check Union/Professional Registers"
8 "Placed or Answered Ads"
9 "Other Active"
10 "Looked at Ads"
11 "Attended Job Training Programs/Courses"
13 "Other Passive"
97 "No Additional Job Search Activities"
;
label define labelturetot
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
3 "Was not retired last time"
;
label define labeltuspabs
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
3 "Retired"
4 "Disabled"
5 "Unable to work"
;
label define labeltuspusft
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
3 "Hours vary"
4 "No longer has a job"
;
label define labeltuspwk
-1 "Blank"
-2 "Don't Know"
-3 "Refused"
1 "Yes"
2 "No"
3 "Retired"
4 "Disabled"
5 "Unable to work"
;
 
label values teabsrsn labelteabsrsn;
label values teernhry labelteernhry;
label values teernper labelteernper;
label values teernrt labelteernrt;
label values teernuot labelteernuot;
label values tehrftpt labeltehrftpt;
label values teio1cow labelteio1cow;
label values telayavl labeltelayavl;
label values telaylk labeltelaylk;
label values telfs labeltelfs;
label values telkavl labeltelkavl;
label values telkm1 labeltelkm1;
label values temjot labeltemjot;
label values teret1 labelteret1;
label values teschenr labelteschenr;
label values teschft labelteschft;
label values teschlvl labelteschlvl;
label values tespempnot labeltespempnot;
label values trdpftpt labeltrdpftpt;
label values trdtocc1 labeltrdtocc1;
label values tremodr labeltremodr;
label values trernupd labeltrernupd;
label values trhernal labeltrhernal;
label values trhhchild labeltrhhchild;
label values trholiday labeltrholiday;
label values trimind1 labeltrimind1;
label values trlvmodr labeltrlvmodr;
label values trmjind1 labeltrmjind1;
label values trmjocc1 labeltrmjocc1;
label values trmjocgr labeltrmjocgr;
label values trnhhchild labeltrnhhchild;
label values trohhchild labeltrohhchild;
label values trspftpt labeltrspftpt;
label values trsppres labeltrsppres;
label values trwbmodr labeltrwbmodr;
label values trwernal labeltrwernal;
label values tthr labeltthr;
label values ttot labelttot;
label values ttwk labelttwk;
label values tuabsot labeltuabsot;
label values tubus labeltubus;
label values tubus1 labeltubus1;
label values tubus2ot labeltubus2ot;
label values tudiaryday labeltudiaryday;
label values tudis labeltudis;
label values tudis1 labeltudis1;
label values tudis2 labeltudis2;
label values tuecytd labeltuecytd;
label values tuelder labeltuelder;
label values tuelfreq labeltuelfreq;
label values tufwk labeltufwk;
label values tuio1mfg labeltuio1mfg;
label values tuiodp1 labeltuiodp1;
label values tuiodp2 labeltuiodp2;
label values tuiodp3 labeltuiodp3;
label values tulay labeltulay;
label values tulay6m labeltulay6m;
label values tulayavr labeltulayavr;
label values tulaydt labeltulaydt;
label values tulk labeltulk;
label values tulkavr labeltulkavr;
label values tulkdk1 labeltulkdk1;
label values tulkdk2 labeltulkdk2;
label values tulkdk3 labeltulkdk3;
label values tulkdk4 labeltulkdk4;
label values tulkm2 labeltulkm2;
label values tulkm3 labeltulkm3;
label values tulkm4 labeltulkm4;
label values tulkps1 labeltulkps1;
label values tulkps2 labeltulkps2;
label values tulkps3 labeltulkps3;
label values tulkps4 labeltulkps4;
label values turetot labelturetot;
label values tuspabs labeltuspabs;
label values tuspusft labeltuspusft;
label values tuspwk labeltuspwk;
 
describe, short;
