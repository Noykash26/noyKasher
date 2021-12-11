from flask import Flask, redirect, url_for, render_template

app = Flask(__name__) # we will work on one instanse of the class Flask


# העטיפה של פונקציה בפייתון, אני עושה פעולות לפני הפונקציה ופעולות אחרי הפונקציה.
# הדיקורייטור זה ההחלפת נעליים לפני ואחרי שמשחקים בבאולינג.
# במקרה שלנו, השרת מקבל בקשה של משתמש להיכנס לאתר, זה מגיע לפונקציה, הדיקורייטור הופך את זה לשפת פייתון, הוא מכין את העמוד, והוא מחזיר בחזרה לHTML
# הדיקוריייטור מעבד מHTML לפייתון ובחזרה.
@app.route('/home_page')
@app.route('/home')
@app.route('/')  # ראוט ראשי משם מתחילים
def hello_fun():
    # return 'welcome to the main page'
    found = True # משל לחיפוש אובייקט בבסיס נתונים
    if found:
        return render_template('index.html', name='Noy')
    else:
        return render_template('index.html')

@app.route('/about', methods = ['GET', 'POST']) # only 'post' is not allowed
def about_fun():
    # TODO # מוסכמה לכך שצריך להשלים כאן קוד
    # DO SOMTHING WITH DB
    # print('i am in about') # הפעולה האלה נעשות למרות שהלקוח לא נוחת בדף
    # return redirect('/catalog')
    # return redirect(url_for('catalog_fun')) # אפשר גם לפונקציה עצמה, יותר נפוץ
    return render_template('about.html',
                           profile={'name': 'Noy', 'second_name': 'kasher', 'city' : 'Givatayim'},
                           university='BGU',
                           degrees=['BSc', 'MSc'],
                           hobbies=('art', 'music', 'sql', 'flask', 'animals', 'web'))

@app.route('/catalog') #נלמד בהמשך איך לעשות את זה יותר דינמי וגנרי שיקבל איזשהו משתנה
def catalog_fun():
    #return 'welcome to catalog page'
    return render_template('catalog.html')

if __name__ == '__main__':
    app.run(debug=True)


# python VS SQL
# get - select, to receive an information
# post - insert, facebook or sign up, we deliver information
# put - update, we deliver information
# delete - delete