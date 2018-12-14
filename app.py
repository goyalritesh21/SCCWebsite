from flask_sqlalchemy import SQLAlchemy
from flask import *
from flask_cors import CORS

SCC = Flask(__name__)
SCC.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SCCData.db'
SCC.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(SCC)
CORS(SCC)


class Users(db.Model):
    __tablename__ = 'Users'

    Name = db.Column(db.VARCHAR(40), nullable=False)
    SID = db.Column(db.String(8), nullable=False, primary_key=True)
    Mobile = db.Column(db.String(10), nullable=False)
    MobileVerified = db.Column(db.BOOLEAN, nullable=False)

    def __repr__(self):
        return '(Name: ' + self.Name + ' SID: ' + str(self.SID) + ' Mobile: ' + str(self.Mobile) + ' Mobile Verified: ' + str(self.MobileVerified) + ' )'


@SCC.route('/')
def hello_world():
    return render_template("Landing_page.html")


@SCC.route('/otp', methods=['POST', 'GET'])
def send_otp():
    result = False
    if request.method == 'POST':
        data = request.form
        print(data)
        if data:
            Name = data['Name']
            SID = str(data['SID'])
            print(SID)
            Mobile = str(data['Mobile'])
            MobileVerified = False
            user = Users(Name=Name, SID=SID, Mobile=Mobile, MobileVerified=MobileVerified)
            curr_session = db.session
            try:
                curr_session.add(user)
                curr_session.commit()
                result = True
            except:
                curr_session.rollback()
                curr_session.flush()
                result = False
        elif data is None:
            return render_template('Landing_page.html', message="Data invalid")
    else:
        return render_template('Landing_page.html', message="Invalid Method")

    if result:
        return render_template('Questions.html')
    else:
        return render_template('Landing_page.html', message="Some unknown error occured.")


if __name__ == '__main__':
    SCC.run(debug=True)
