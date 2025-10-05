from website import create_app
from website import rename_columns_with_sql
 
app = create_app()

if __name__ == '__main__':
    app.run(debug=True) 