Layer--xml
	Linear Layout
	Relative Layout

	TextView



Android�������Ϊxml��ʽ�������resĿ¼��

	android:layout_width // ������--match_parent��������parent
	android:layout_height // ����߶�--match_parent��������parent

	android:id // ����Ψһ��ʶ
	
values/string.xml
	���ַ�����name="key">value<��ʽд��ŵ��У��ڴ�����Ƶ�xml��ʹ��@string:key����
	

Context:
	Context���ǳ����࣬�ṩ��һ��ͨ�õ�POI���ڷ���Ӧ�ó���ȫ����Ϣ��һЩӦ�ü�����ࣨAndroid�ڲ��ࣩ���̳���Context
	��Contextʵ������ = Service���� + Activity���� + 1��Application��Ӧ��Contextʵ����
Activity:
	һ��Activity��Ӧһ��Ӧ�ó�����棬������������Activity����ת����
	����������startActivity() / startActivityForResult()
	�ṩonCreate(), onStart()�ӿڣ���Activity����ʱ���ص�

Service:
	Ӧ�õĺ�̨�����������ڲ�ȡ����ĳ��Activity��
	����������startService() / bindService()

Intent:
	������Ļ�����л������������֡������������͡����ݣ�URL��ʾ����������
	IntentFilter:
		��������һ��Activity/IntentReceiver�ܹ�������Щintent
		��Ҫ��AndroidMainifest.xml�ж�����ôȥ����View������URL����startActivity()����ʱ����ȥ������Ӧ��xml����������Ӧ������
	IntentReceiver:
		InetnetReceiver���Զ�ϵͳ�¼�����Ӧ�����¼�����ʱ����NotificationManager֪ͨ�û�
		��AndroidMainifest.xml��ע�� ��Ҳ������Context.registerReceiver()ע��
		ʹ��Context.broadcastIntent()���Խ��¼��㲥����������
Content Provider��
	����AndroidӦ��֮�䴫�����ݣ���ĳӦ�ö�ͨѶ¼��΢������


Android�ṩ��API
android.app ���ṩ�߲�ĳ���ģ�͡��ṩ���������л���
android.content ���������ֵĶ��豸�ϵ����ݽ��з��ʺͷ�������
android.database ��ͨ�������ṩ������Ͳ������ݿ�
android.graphics ���ײ��ͼ�ο⣬������������ɫ���ˣ��㣬���Σ����Խ�����ֱ�ӻ��Ƶ���Ļ��.
android.location ����λ����ط������
android.media ���ṩһЩ����������Ƶ����Ƶ��ý��ӿ�
android.net ���ṩ����������ʵ��࣬����ͨ���� java.net.* �ӿ�
android.os ���ṩ��ϵͳ������Ϣ���䡢IPC ����
android.opengl ���ṩ OpenGL �Ĺ���
android.provider ���ṩ����� Android �������ṩ��
android.telephony ���ṩ�벦��绰��ص� API ����
android.view ���ṩ�������û�����ӿڿ��
android.util ���漰�����Եķ���������ʱ�����ڵĲ���
android.webkit ��Ĭ������������ӿ�
android.widget ���������� UI Ԫ�أ��󲿷��ǿɼ��ģ���Ӧ�ó������Ļ��ʹ��


JVM��Dalvik�����

.java Դ�ļ�
.class Ŀ���ļ�(�޷���Android Dalvik��ִ��,��Ҫ���ӳ�dex�ļ�)
.dex Android�ϵĿ�ִ���ļ�
.apk Android�ϵİ�װ�ļ��������AndroidMainifest.xml��dex����Դ�ļ��������ļ�










