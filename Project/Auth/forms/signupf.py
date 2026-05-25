from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,PasswordField,SubmitField,SelectField
from wtforms.validators import DataRequired,Email,EqualTo

class SignUp(FlaskForm):
    firstName = StringField("الاسم الأول:",validators=[DataRequired()])
    lastName=StringField("الاسم الأخير:",validators=[DataRequired()])
    Email = EmailField("الايميل:",validators=[DataRequired(),Email()])
    university = SelectField("الجامعة:",validators=[DataRequired()],choices=[
    # الجامعات الحكومية
    "جامعة القاهرة",
    "جامعة عين شمس",
    "جامعة الإسكندرية",
    "جامعة حلوان",
    "جامعة المنصورة",
    "جامعة الزقازيق",
    "جامعة أسيوط",
    "جامعة طنطا",
    "جامعة بنها",
    "جامعة الفيوم",
    "جامعة سوهاج",
    "جامعة كفر الشيخ",
    "جامعة المنوفية",
    "جامعة قناة السويس",
    "جامعة بني سويف",
    "جامعة جنوب الوادي",
    "جامعة بورسعيد",
    "جامعة دمياط",

    # الجامعات الخاصة والأهلية
    "الجامعة الألمانية بالقاهرة",
    "الجامعة الأمريكية بالقاهرة",
    "جامعة مصر للعلوم والتكنولوجيا",
    "جامعة 6 أكتوبر ",
    "جامعة المستقبل",
    "جامعة بدر",
    "جامعة النيل",
    "جامعة زويل للعلوم والتكنولوجيا",
    "جامعة الجلالة",
    "جامعة العلمين الدولية",
    "جامعة المنصورة الجديدة",
    "جامعة الملك سلمان الدولية"
])
    major = SelectField("التخصص:",validators=[DataRequired()],choices=["اخر","حاسبات","هندسة قسم الحاسب","علوم قسم حاسب"])
    Password = PasswordField("كلمة المرور:",validators=[DataRequired(),EqualTo('confpass')])
    confpass = PasswordField("تأكيد كلمة المرور:",validators=[DataRequired()])
    submit = SubmitField("Submit")
# hello , my mdnowifjdjnlsjksdjsjdojdiewjdwiejdweijdweijdweidwejdwepjdweiofjiwefjiwefjewifjweoifjeifjweofijweoifjweiofjweifjeifjeifjeifjeifjeifjwifwjfiwefjeifjweifjweifewifjewifjweifweifewjfiwefj
#TODO: eating taco
