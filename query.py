"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?
    # A query object of flask_sqlalchemy.BaseQuery (not Brand object)

# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?
    # An association table is a table that does not have any useable colums 
    # other than foreign keys from other tables
    # It deals with many to may relationships

# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
# q1 = Brand.query.filter_by(brand_id='ram').first()
q1 = Brand.query.get("ram")

# # Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = Model.query.filter_by(name='Corvette', brand_id='che').all()

# # Get all models that are older than 1960.
q3 = Model.query.filter(Model.year < 1960).all()

# # Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()

# # Get all models with names that begin with ``Cor``.
q5 = Model.query.filter(Model.name.like('Cor%')).all()

# # Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# # Get all brands that are either 1) discontinued (at any time) or 2) founded
# # before 1950.
q7 = (Brand.query.filter((Brand.discontinued.isnot(None)) | 
                         (Brand.founded < 1950)).all())

# # Get all models whose brand_id is not ``for``.
q8 = Model.query.filter(Model.brand_id != 'for').all()



# -------------------------------------------------------------------
# Part 4: Write Functions

def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""
    
    print "Models from " + str(year)
    models = Model.query.filter(Model.year == year).all()

    # # Solution 1
    # result = {}
    # for model in models:
    #     brand_info = (str(model.brand.name), str(model.brand.headquarters))
    #     if brand_info in result:
    #         result[brand_info].append(model.name)
    #     else:
    #         result[brand_info] = [str(model.name)]

    # import pprint
    # pprint.pprint(result)
    # del pprint

    # Solution 2
    print "\n\n----------------- {year} -----------------".format(year=year)
    if models:
        for model in models:
            result_str = "{brand} {model} ({HQ})"
            print result_str.format(brand=model.brand.name,
                                    model=model.name,
                                    HQ=model.brand.headquarters)
        print
    else:
        print "No models from that year in the database\n"


def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""

    # # Solution 1

    # brands = (db.session.query(Brand.name, Model.name, Model.year).
    #          join(Model).all())
    # result = {}

    # for brand in brands:
    #     b_name, m_name, yr = str(brand[0]), str(brand[1]), str(brand[2])
    #     if b_name in result:
    #         result[b_name].append(m_name + " (" + yr + ")")            
    #     else:
    #         result[b_name] = [m_name + " (" + yr + ")"]

    # import pprint
    # pprint.pprint(result)
    # del pprint

    # Solution 2

    all_brands = Brand.query.all() # Use the relationship to bring all

    for brand in all_brands:
        print "\n{brand}".format(brand=brand.name)
        print "-" * 25
        if brand.models:
            for model in brand.models: # Because of the relationship, you can reach into models
                print "  {year} {model}".format(year=model.year,
                                                model=model.name)
        else:
            print "  None\n"
    print


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    # returning objects, not printing results as asked
    return Brand.query.filter(Brand.name.like('%' + mystr + '%')).all()


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    # returning object not printing resultm as requested
    return Model.query.filter(Model.year >= start_year, Model.year < end_year).all()


# def test_query_dot_py():

#     print "--------Printing test cases for query.py--------\n"

#     print "This is test case running for get_model_info function"
#     get_model_info(1963)
#     print "End of test case\n"

#     print "This is test case running for get_brands_summary function"
#     get_brands_summary()
#     print "End of test case\n"

#     print "This is test case running for search_brands_by_name(mystr)"
#     print search_brands_by_name('a')
#     print "End of test case\n"

#     print "This is test case running for get_models_between(start_year, end_year)"
#     print get_models_between(1920, 1950)
#     print "End of test case\n"

#     print "--------End printing test cases for query.py--------"


# test_query_dot_py()