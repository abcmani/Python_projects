import random
import string

file= open('GeneratedInserts.txt','w')

for i in range(1,1000):
    file.write("""Insert into TRB1_PUB_LOG (SOURCE_COMP_ID,PUB_TRX_ID,SYS_CREATION_DATE,SYS_UPDATE_DATE,OPERATOR_ID,APPLICATION_ID,DL_SERVICE_CODE,DL_UPDATE_STAMP,GROUP_TRX_SEQ_NO,ACTV_CODE_ID,REQ_NOTIFY_CD,LEN_BEFORE_COMP,GENERAL_DATA,GENERAL_DATA_C,BUFFER_ID,ENTITY_TYPE,ENTITY_ID,UNI_LOB_ACT_SIZE,AUDIT_INTERVAL,CORRELATION_ID,GENERAL_FIELD_NUM,GENERAL_FIELD_STRING,PART_DEP_ENT,CRE_DEP_ENT,AUDIT_INDICATOR,AUDIT_SEQ_NUM,SOURCE_CRE_DATE,ADDITIONAL_FILTER,DISTRIBUTION_TYPE,ASYNC_IND) values (2003,"""+str(4200+i)+""",to_date('10-MAY-19','DD-MON-RR'),null,0,'A-JAV ','JAV01',null,null,9021,'N ',0,'<?xml version="1.0" encoding="ISO-8859-15" ?>
<TRB_TRX xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<HEADER AckInd="0" ReqNotf="N" Priority="2" TransactionCode="L9_DANE_THRESH_NOTIF_REQ" PublisherApplID="RLC" PublisherApplThreadID="1" IssueDate="2019-04-06T23:59:59" EffectiveDate="2019-04-06T23:59:59" RoutingId="100000042" EntityId=\""""+str(11+i)+"""\" EntityType="CUSTOMER"/>
	<DATA>
		<ThresholdInfo>
			<PlanAPID>"""+str(43525714+i)+"""</PlanAPID>
			<planLevelIndicator>"""+random.choice("SG")+"""</planLevelIndicator>
			<triggerName>"""+''.join(random.choice(string.ascii_uppercase) for _ in range(8))+"""</triggerName>
			<date>2019-04-06T23:59:59</date>
		</ThresholdInfo>
	</DATA>
</TRB_TRX>', EMPTY_CLOB(),-1,null,null,0,null,null,0,'RESOURCE','customer="""+str(11+i)+""";','customer="""+str(11+i)+""";','N',null,null,null,null,'N');\n""")

file.close()
