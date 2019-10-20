import datetime
import re
import string

def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)
    
    return  mainString     

def main():
    running = True
    now = datetime.datetime.now()
    strnow = now.strftime("%X") #current time
    #log file date
    fileDate = now.strftime("%d-%b-%Y")
    fileName = "trapd-" + fileDate + ".log"
    output = open('/home/bass/trap-receiver/' + fileName, 'a')
    
    while running:
        try:
            input = raw_input()
            filtered = input.replace("<UNKNOWN>","" )
            showDate = filtered.replace("UDP: [172.30.232.2]:32768->[172.30.232.250]:162", strnow)
        
            wronglist = ['Wrong Type (should be Gauge32 or Unsigned32)', 'Wrong Type should be Timeticks:','Wrong Type should be OCTET STRING:'
            ,'Wrong Type should be Timeticks:','Wrong Type should be OCTET STRING:']

            wrongtypeRemove = replaceMultiple(showDate, wronglist, '')
            timestamp = wrongtypeRemove.replace("DISMAN-EVENT-MIB::", "")
            mibList = ['SNMPv2-MIB::','CISCO-LWAPP-SI-MIB::','CISCO-LWAPP-RRM-MIB::',
            'CISCO-LWAPP-ROGUE-MIB::','AIRESPACE-WIRELESS-MIB::',
            'CISCO-LWAPP-DOT11-CLIENT-MIB::','CISCO-LWAPP-AP-MIB::','CISCO-LWAPP-AP-MIB::','CISCO-LWAPP-RF-MIB::','CISCO-LWAPP-WLAN-MIB::']
            hideMIB = replaceMultiple(timestamp, mibList, '')
            event = hideMIB.replace("snmpTrapOID","Event")
            prefixList = ['bsn','cL','cldc','Dot11','Dot3','AirespaceAP','ciscoLwapp','sys','SiIdr','Si','clrRrm']
            weirdList = ['.0',". ",'.1 ','"',' : ']
            prefixRemove = replaceMultiple(event, prefixList, '')
            weirdRemove = replaceMultiple(prefixRemove, weirdList, ' ')
            bad_chars = "/\\!$^&*|'({)[}>_<]~+=#$%;`@?"
            #rgx = re.compile('[%s]' % bad_chars)
            # pattern = "^.A-Za-Z0-9'&{8,9}"
            # replace = ''
            #outstr
            bad_list = ['.......','..N...','.t....','..N..i.','..V...','..:..j',
            '......f','......','..a.bk','    .','....np','..N..j.','.hx.G','...z.A.','..p-:.e'
            ,'.p....','.p..6s','. G..U.','. y.c..','...7L..','...6..','.....','.P....','.tp.s6.','....:2.','.hx...','.Tb.3..','.H..8.'
            ,'.d...Z.','.0...,j','.....M','....i.','..lcQZ.','...h.R','....s.','.0.M...','.....uj','....T..','..8pw..','..o.-p','..xABn.'
            ,'.X..VM.','.D.F','...ci5.','....b.2','.X..Yy.','...x..s','.....O.','....56','..E..','.M..v.','.D.F...','....P.','.X..Q..'
            ,'...z...','.x.mO..','...3..','.0.....','...W..','.L.1.o','...-..w','....W.g','....A..','.X.....','.4BbD.','.0...a.','.8...-P',
            '.4-...','...E..','...WfKe','.T.:...','..bgFH.','. ....','..Wu..','..f.4hZ','....wA','...g.i.','..Vw.','..p-...','.,..6U.','..N..e.'
            ,'.H...s','.d.SB..','.pim.z','..w....','...M.','....l.','..d....','..n..','.pp.cA.','..yp..9','.t...H','.M....','.....Y.','..f..A'
            ,'.....v','..-.:m','..y...K','..E.x','.h....K','.D.,..','.p...n','..6....','.0.k...','.....9.','....N.','.L.f.G','.H.....','....3..'
            ,'.L..v','.0.T...','.4..cF','...p..e','..5.w..','.H...','...1.i.','..8p...','.hx.F','...v.b','.Df....','..E...','...D','.D...R.'
            ,'....8.','..-...','...','..Dc..','..6.Wh.','.xOC...','..4j...','..,...','...C..E','.XNd..','...b...','.....c.','.t...a','...h'
            ,'....:jn','..6.NE.','.....n.','....','..6.P..','.....C','.D..o8','.0..U.','..a...x','.k..l.','.x1.p.','.....e','.4...c.','.P..N.'
            ,'..x..2','.....X','..3..z.','...7L..:','.....,','..Z....','..J...M','..6.L:.','.t..M.P','...h...','.,..N..','..u....','..o.o0.'
            ,'.. ..','.l.k,..','.xOC.k3','.XN..','...W...','....I..','..PF.P','.....r','.pp....','.t...Y.','.....j','.x..u.','.....y.'
            ,'..A..v.','....i..','.:','...i..','.h..1:S','....4.','..o...','..mR...','.Lk....','..N..N.','.,a....','.....-.','..o1..'
            ,'.hT....','......    .','..k.7.9','.0.r.','CX..','.Z.','..z..u','..Ag','.Tb..q','.t.OxE.','..YqWR','.t..c.w','..YqWR','..UX'
            ,'.t..c.w','..PF..','-.','.l..oT','.xaZ..','.vE.','.8-.','.Tb..G','.Q.','.V5','t..','..','.0.','..S','V.Oj','.vE.','.z..','.pv.'
            ,'QY.','.N6.3.','7.N','.zO.','..PF..','.Df..z.','f.f','6.N','.4Bb','B.HT','o.l','g.','.D.M','cx','.z','.8q.m','.Lk','.LPuY'
            ,'.,a.5','.TrOi','.Lk.',',.2.','.LV.v.K','R.','.,V.','.hT.','.05.','.V.','lt.','E.','.7.','.H','6.J','F.','.pa.','c.I.','.xOC'
            ,'.p.','.H.k.x',',.','.k.x','.P','i.','.b1','VM','.8i','.kV','.lMs.e.','u.r','.S.','.BO','cv.','.Dn6','.L.q','J',' ','.8qX'
            ,' O.','N.','Q.','k.','.f.a','.L.q',' h ','CG','.TbA.','V.','.W','.o.Y','.X','.K0.','.TrO5','.4.-Y.',' . ','.  ','S.','.L.1ItK',' Z ',' np '
            ,'  a ','.hT','l.Y.','  .3 ',' K   ',' p ',' U. ',' .5. ',' t. ',' .vj ','.h.2  ',' m ',' D ',' D. ',' 4.C. ',' Wd.K ',' 1.x '
            ,'.p:Q  ',' C ',' f. 1 ',' .c  ','.dp3  ','  ','.0 y5 ',' 3.d. ','.8 ','.3 ']
            outstr  = weirdRemove.translate(None, bad_chars)
            result = replaceMultiple(outstr,bad_list,' ')

            output.write(result + '\n')

        except EOFError:
            running = False
    output.close()
if __name__ == '__main__':
    main()
