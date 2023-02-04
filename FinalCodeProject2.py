#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jenna Lee and Catarina Bettencourt

DS 20001_Fall2022

Date: 12/01/2022
    
File: .py

Description: This program compares GDP to Winter and Summer Olympic medals 
for different competing countries from 1896 to 2016. This program also visualizes 
the location of Olympic medals for both Summer and Winter games.

"""
# imports
import matplotlib.pyplot as plt

# data files to be referenced
ATHLETE_FILE = "athlete_events_updates.csv"
GDP_FILE = "countries_GDP_updated.csv"
LOCATION = "location_updated.csv"

def read_in_test(filename):
    """
    Reads in data as list of lists.
    Stores the values in a list of lists of strings (by default).
    Assumes that commas separate row items in the given file.
    
    Parameters
    ----------
    filename : string
        name of the file

    Returns
    -------
    data : list of lists
        list of lists of values for lines in the file
    """
    file = open(filename, "r")
    headers = file.readline()
    data = []
    for line in file:
        s_data = []
        pieces = line.strip().split(",")
        # ID,Name,Sex,Age,Height,Weight,Team,NOC,Games,Year,Season,City,Sport,Event,Medal
        if pieces[14] != "NA":
            s_data.append(pieces[6])
            s_data.append(pieces[14])
            s_data.append(pieces[10])
            

            data.append(s_data)
        
    file.close()
    return data

def read_in_spec(filename, pop1, pop2):
    """
    Reads in data as a list of lists.
    Specifies an index of file to remove from list
    
    Parameters
    ----------
    filename : string
        name of the file
    pop1 : integer
        index number of item designated to be removed from
        
    pop2 : integer
        index number of item designated to be removed from

    Returns
    -------
    data : list of lists
        list of lists of values for lines in the file, 
        does not contain popped items
    """
    file = open(filename, "r")
    headers = file.readline()
    data = []
    for line in file:
        pieces = line.strip().split(",")
        pieces.pop(pop1)
        if pop2 != None:
            pieces.pop(pop2)
        data.append(pieces)
    '''

    DS2001
    
    Practicum1
    
    Catarina Bettencourt
    
    Consulted simplilearn for pop function:  
    
    https://www.simplilearn.com/tutorials/python-tutorial/pop-in-python#:~:text=List%20pop%20in%20Python%20is,last%20element%20of%20the%20list
    
    '''
    file.close()
    return data

def countries(data):
    """
    Reads in data as a list of lists. 
    Converts certain elements into floats. 
    
    Parameters
    ----------
    data : list of lists
        list of lists of values for lines in the file

    Returns
    -------
    new_data: list of lists
        updated list of lists of values for lines in the file
    """
    new_data = []
    for line in data:
        pieces = []
        for i in range(len(line)):
            if i == 0:
                pieces.append(line[0])
            else:
                pieces.append(float(line[i]))
        new_data.append(pieces)    
    return new_data

def percent_change(data):
    """
    Percent change of values over the years for different countries.
    
    Parameters
    ----------
    data : list of lists
        list of lists of values for lines in the file

    Returns
    -------
    percent_change: float
        list of floats of values for values within different years
    """
    percent_GDP = []
    for line in data:
        pieces = []
        for i in range(len(line)):
            if i == 0:
                pieces.append(line[0])
            elif i != len(line) - 1:
                percent_change = ((line[i + 1] - line[i]) / line[i]) * 100 
                pieces.append(percent_change)
        percent_GDP.append(pieces)
    return percent_GDP

def isolate_best(data):
    """
    Sorting values in a list from highest to lowest positive values.
    Finding the highestest values.
    
    Parameters
    ----------
    data : list of lists
        list of lists of values for lines in the file

    Returns
    -------
    best_GDP: float
        list of floats in order from highest to lowest value
    """
    best_GDP = []
    best_GDP_dict = {}
    for line in data:
        new_line = line[1:]
        new_line.sort(reverse=True)
        highest_GDP = new_line[0]
        best_GDP_dict[highest_GDP] = line[0]
        best_GDP.append(highest_GDP)
    best_GDP.sort(reverse=True)
    return best_GDP
    
def isolate_low(data):
    """
    Sorting values in a list from lowest to highest negative values.
    Finding the lowest values.

    Parameters
    ----------
    data : list of lists
        list of lists of values for lines in the file

    Returns
    -------
    best_GDP: float
        list of floats in order from lowest to highest value
    """
    low_GDP = []
    low_GDP_dict = {}
    for line in data:
        new_line = line[1:]
        new_line.sort(reverse=False)
        lowest_GDP = new_line[0]
        low_GDP_dict[lowest_GDP] = line[0]
        low_GDP.append(lowest_GDP)
    low_GDP.sort(reverse=False)
    return low_GDP

def count(data, season):
    """
    Counts medals for a specific country 

    Parameters
    ----------
    data : list
        list of lists of values for lines in the file
    season : string
        list of options for "Summer", "Winter", or "Both"

    Returns
    -------
    count_vals : list of dictionaries
        list of dicts of values for all lines in the file
        example {"country": name of country, "medal_count" : associated sum of medals}
    """
    count_vals = []
    items_lis = []
    test_list = []
    
    for line in data:
        if season == "Summer":
            if line[2] == "Summer": 
                items_lis.append(line[0])
        if season == "Winter":
            if line[2] == "Winter": 
                items_lis.append(line[0])           
        if season == "Both":
            items_lis.append(line[0])
    for item in items_lis:
        if item not in test_list:
            test_list.append(item)
            dic = {}
            count = items_lis.count(item)
            dict1 = {"country" : item}
            dict2 = {"medal_count" : count}
            dic.update(dict1)
            dic.update(dict2)
            count_vals.append(dic)
    return count_vals

def extract_dict(data, column):
    """ 
    Extract a column of data from a 2D dictionary
    
    Parameters
    ------
    data : list 
        list of lists
    column : strings
        column index to be extracted
    
    Returns
    ------
    col : list 
        list values from a certain index
    """
    col = []
    
    for piece in data:
        col.append(piece.get(column))
    
    return col

def extract_l(data, column_num):
   """ 
   Extract a column of data from a 2D dictionary
   
   Parameters
   ------
   data : list 
       list of lists
   column_num : integer
       column index to be extracted
   
   Returns
   ------
   col : list 
       list of values from a certain index
   """
   col = []
    
   for piece in data:
       col.append(float(piece[column_num]))
    
   return col

def finder(data1, data2, key, test, cast, column):
    """ 
    Finding the values from one data set and matching it to the corresponding
    values from another set. Uses key and test to determine if match exists.
    
    Parameters
    ------
    data1 : list of dictionaries
        list of dicts of values for lines in the file
    data2 : list 
        list of lists of values for lines in the file 
    key : string
        indicates key in dictionary to use for match test
    test : integer
        index of row in data2 to use for match test
    cast : type 
        type that appended items should be cast as
    column : integer
        index of row to be appended to final dataset
    
    Returns
    ------
    lis : list
        list of appended items, type depends on data2
    """
    lis = []
    for item in data1:
        for piece in data2:
            if item.get(key) == piece[test]:
                lis.append(cast(piece[column]))
    return lis

def topten(data, direction, listordict, testval):
    """ 
    List of top values that are either above or below the specified test value.
    
    Parameters
    ------
    data : list 
        list of values for lines in the file
    direction : string 
        string called for values to be extracted
        options are "top" or "bottom"
    listordict: list or dictionary
        list or dictionary called from the file
    testval : integer
        value to test items against

    
    Returns
    ------
    n_list : list of dictionaries
        list of dicts of values for all lines in the file
    """
    n_list = []
    if direction == "top":
        for piece in data:
            if listordict == "dictionary":
                if piece.get("medal_count") > testval:
                    n_list.append(piece)
            else:
                if piece != None:
                    if piece > testval:
                        index = data.index(piece)
                        n_list.append(index)
    if direction == "bottom":
        for piece in data:
            if listordict == "dictionary":
                if piece.get("medal_count") < testval:
                    n_list.append(piece)
            else:
                if piece != None:
                    if piece < testval:
                        index = data.index(piece)
                        n_list.append(index)
    return n_list

def listfinder(data, indexlist1, indexlist2):
    """ 
    Finds the list to be extracted 
    
    Parameters
    ------
    data : list 
        list of values for lines in the file
    indexlist1 : list 
        list of integers 
    indexlist2: list 
        list of integers 
    
    Returns
    ------
    n_list : list
        list of values that contains data from both lists of indexes
    """
    n_list = []
    for item in indexlist1:
        n_list.append(data[int(item)])
    for item in indexlist2:
        n_list.append(data[int(item)])
    return n_list

def organize(list1, cat1, res1, cat2, res2, cat3, res3, cat4, res4, res5, res6):
    """ 
    Determining the color and sizes of points depending on parameters
    
    Parameters
    ------
    list1 : list 
        list of integers of values for lines in the file
    cat1 : integer 
        integer to test against against value in list1 
    res1 : integer or string
        desired value that results if cat1 is satisfied, in this code, 
        used to assign size or color for plotted point 
    cat2 : integer 
        integer to test against against value in list1 
    res2 : integer or string 
        desired value that results if cat1 is satisfied, in this code, 
        used to assign size or color for plotted point 
    cat3 : liintegerst 
        integer to test against against value in list1 
    res3 : integer or string 
        desired value that results if cat1 is satisfied, in this code, 
        used to assign size or color for plotted point 
    cat4 : integer 
        integer to test against against value in list1 
    res4 : integer or string 
        desired value that results if cat1 is satisfied, in this code, 
        used to assign size or color for plotted point 
    res5 : integer or string 
        desired value that results if cat1 is satisfied, in this code, 
        used to assign size or color for plotted point 
    res6 : integer or string 
         desired value that results if cat1 is satisfied, in this code, 
         used to assign size or color for plotted point 
         
    Returns
    ------
    result : list
        list of results determined by how which catetgory a value satisfied, 
        used in this code to make a list of sizes or colors thagt corresponded 
        to plotted points
    """
    result = []
    for item in list1:
        if item != None:
            if item < cat1:
                result.append(res1)
            if cat1 < item < cat2:
                result.append(res2)   
            if cat2 < item < cat3:
                result.append(res3)
            if cat4 != None and cat3 < item < cat4:
                result.append(res4)
            if cat4 != None and item > cat4:
                result.append(res5)
        else:
            result.append(res6)
    return result
        
def averager(data):
    """ 
    Calculating the average data for the GDP of each years in a country
    
    Parameters
    ------
    data : list 
        list of lists of values for lines in the file
        
    Returns
    ------
    ave_data : list of dictionaries
        list of dicts for the average GDPs for each country
    """
    ave_data = []
    for row in data:
        vals = {}
        country = row[0]
        row.pop(0)
        ave = sum(row) / len(row)
        dict1 = {"country" : country}
        dict2 = {"average" : ave}
        vals.update(dict1)
        vals.update(dict2)
        ave_data.append(vals)
    return ave_data

def matcher(dict1, dict2, key1, key2, cast, column):
    """ 
    Matches desired values from two dictionaries according to specified value, 
    (overall, countries were used as the matching value for this code)
    
    Parameters
    ------
    dict1 : list of dictionaries 
        list of dictionaries for countries and medal count 
    dict2 : list of dictionaries
        list of dictionaries with average GDPs 
    key1: string 
        name of key to be called
    key2 : string 
        name of key to be called
    cast : type 
        type that appended items should be cast as
    column : integer 
        index number of item in list to be appended
    
    Returns
    ------
    lis : list
        list of values for countires and top ten GDPs
    """    
    lis = []
    for item in dict1:
        found = False
        for piece in dict2:
            if item.get(key1) == piece.get(key2):
                found = True
                lis.append(cast(piece[column]))
        if found == False:
            lis.append(None)
    return lis


def generate_region(title, yesorno, x_axis, y_axis, size, colors, smaller, imagename):
    """
    Generates visualization of world based on specified values

    Parameters
    ----------
    title : string
        string name of visualization
    yesorno: Boolean
        indicates if a legend is necessary
        True value will plot legend
    x_axis : list
        list of values to plot x-axis
        x-axis label
    y_axis : list
        list of values to plot y-axis
        y-axis label
    size : list
        list of integers for marker size, corresponds to number of medals one
    colors : list
        list of strings for color in visualization, 
        corresponds to average percent of gdp
    smaller : boolean
        True indicated to plot within a limited range,
        False indicated to plot within full range
    imagename: string
        string to save image as a png file
        
    Returns
    -------
    None.
    """
    # clear figure
    plt.clf()
    
    # plot settings
    plt.title(title)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    
    if smaller == True:
        plt.xlim(-45, 60)
        plt.ylim(20, 90)
        plt.scatter(y_axis, x_axis , s = size, color = colors)
        
        # plot colors for legend
        plt.plot(200, -90, ".", color = "darkred", markersize = 10, 
                 label = "Extremely Low Increase in Percent Change in GDP (<6%)")
        plt.plot(200, -90, ".", color = "darkorange", markersize = 10, 
                 label = "Low Increase in Percent Change in GDP (<7%)")
        plt.plot(200, -90, ".", color = "gold", markersize = 10, 
                 label = "Average Increase in Percent Change in GDP (<9%)")
        plt.plot(200, -90, ".", color = "yellowgreen", markersize = 10, 
                 label = "High Increase in Percent Change in GDP (<11%)")
        plt.plot(200, -90, ".", color = "darkgreen", markersize = 10, 
                 label = "Extremely High Increase Percent Change in GDP (>11%)")
        plt.plot(200, -90, ".", color = "dimgray", markersize = 10, 
                 label = "Missing Data")
        
        plt.legend(loc = "upper left", prop={'size': 5})
        
        
        plt.text (-4.8380649, 39.3262345, "Spain", size = 5, 
                  bbox = dict(facecolor = "whitesmoke", edgecolor = "lightgray"))  
        plt.text (-3.2765753, 60.7023545, "United Kingdom", size = 5, 
                  bbox = dict(facecolor = "whitesmoke", edgecolor = "lightgray"))  
        plt.text (19.134422, 52.215933, "Poland", size = 5, 
                  bbox = dict(facecolor = "whitesmoke", edgecolor = "lightgray")) 
        
    else:
        
        # axis limits
        plt.xlim(-180, 200)
        plt.ylim(-90, 90)
        
        # plot data
        plt.scatter(y_axis, x_axis , s = size, color = colors)
        
        if yesorno == True:
            # plot colors for legend
            plt.plot(200, -90, ".", color = "darkred", markersize = 10, 
                     label = "Extremely Low Increase in Percent Change in GDP (<6%)")
            plt.plot(200, -90, ".", color = "darkorange", markersize = 10, 
                     label = "Low Increase in Percent Change in GDP (<7%)")
            plt.plot(200, -90, ".", color = "gold", markersize = 10, 
                     label = "Average Increase in Percent Change in GDP (<9%)")
            plt.plot(200, -90, ".", color = "yellowgreen", markersize = 10, 
                     label = "High Increase in Percent Change in GDP (<11%)")
            plt.plot(200, -90, ".", color = "darkgreen", markersize = 10, 
                     label = "Extremely High Increase Percent Change in GDP (>11%)")
            plt.plot(200, -90, ".", color = "dimgray", markersize = 10, 
                     label = "Missing Data")
            # plot legend
            plt.legend(loc = "lower left", prop={'size': 5})
        
        
        # plot text boxes for contintents
        '''
        
        DS2001
        
        Practicum1
        
        Catarina
        
        Consulted stackoverflow for creating text boxes:  
        
        https://stackoverflow.com/questions/17086847/box-around-text-in-matplotlib
        
        '''
        
        plt.text (-110.4458825, 50.7837304, "North America", size = 5, 
                  bbox = dict(facecolor = "whitesmoke", edgecolor = "lightgray"))
        plt.text (-80.2, -10.3333333, "South America", size = 5, 
                  bbox = dict(facecolor = "whitesmoke", edgecolor = "lightgray"))    
        plt.text (0.4234469, 73.0834196, "Europe", size = 5, 
                  bbox = dict(facecolor = "whitesmoke", edgecolor = "lightgray"))   
        plt.text (19.9981227,7.0323598, "Africa", size = 5, 
                  bbox = dict(facecolor = "whitesmoke", edgecolor = "lightgray"))
        plt.text (104.999927,35.000074, "Asia", size = 5, 
                  bbox = dict(facecolor = "whitesmoke", edgecolor = "lightgray")) 
        plt.text (124.755,-24.7761086, "Australia", size = 5, 
                  bbox = dict(facecolor = "whitesmoke", edgecolor = "lightgray"))  
        #plt.text (105, -60, "Individual Olympic Athletes", size = 5, 
                  #bbox = dict(facecolor = "whitesmoke", edgecolor = "lightgray"))
        

        
    # save plot
    plt.savefig(imagename, bbox_inches="tight")
    plt.show()
    
def generate_bar(clear, data1, data2, range1, rotation, colors, title, x_axis, y_axis, imagename):
    """
    Generates bar graph visualization of script

    Parameters
    ----------
    clear : boolean
        True specifies to clear the plot
        False specifies to not clear the plot
    data1 : list 
        list of values from a certain index
    data2 : list
        list of values from a certain index
    range1 : integer
        integer for size of plot
    rotation : integer
        input integer to rotate x-axis labels
    colors : list
        list of strings for color of bars plotted
    title: string
        title of plot
    x_axis : string
        x-axis label
    y_axis : string
        y-axis label
    imagename: string
        string to save image as a png file
        
    Returns
    -------
    None.
    """
    # clear plot 
    if clear == True:
        plt.clf()
        
    # plot settings
    # ---------------
    plt.title(title)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.xticks(rotation = rotation)
    plt.ylim(0, range1)
    
    
    # plot data
    # -----------
    plt.bar(data1, data2, color = colors)
    
    
    # create legend
    # ---------------
    plt.plot(0, 0, ".", color = "darkred", markersize = 10, 
              label = "Extremely Low Increase in Percent Change in GDP (<6%)")
    plt.plot(0,0, ".", color = "darkorange", markersize = 10, 
              label = "Low Increase in Percent Change in GDP (<7%)")
    plt.plot(0,0, ".", color = "gold", markersize = 10, 
              label = "Average Increase in Percent Change in GDP (<9%)")
    plt.plot(0,0, ".", color = "yellowgreen", markersize = 10, 
              label = "High Increase in Percent Change in GDP (<11%)")
    plt.plot(0,0, ".", color = "darkgreen", markersize = 10, 
              label = "Extremely High Increase Percent Change in GDP (>11%)")
    plt.plot(0.0, ".", color = "dimgray", markersize = 10, 
              label = "Missing Data")
    
    plt.legend(prop={'size': 5})
    
    # save and show figure
    # ---------------------
    plt.savefig(imagename, bbox_inches="tight")
    plt.show()


def main():
    # read in files
    athlete_data = read_in_test(ATHLETE_FILE)
    gdp_data = read_in_spec(GDP_FILE, 1, None)
    loc_data = read_in_spec(LOCATION, 1, 1)
    
    # create season specific dictionary containing country and medal count
    all_medal_count = count(athlete_data, "Both")
    win_medal_count = count(athlete_data, "Winter")
    sum_medal_count = count(athlete_data, "Summer")

    # medal count related calculations and code
    country_lis = extract_dict(all_medal_count, "country")
    top_ten_data = topten(all_medal_count, "top", "dictionary", 900)


    # gdp related calculations and code
    gdp = countries(gdp_data)
    percent = percent_change(gdp)
    country_gdp = matcher(all_medal_count, averager(percent), "country", 
                          "country", float, "average")
    top_5_index = topten(country_gdp, "top", list, 10)
    low_5_index = topten(country_gdp, "bottom", list, 6.5)

    
    # generate bar graphs
    # ---------------------
    # medal count graph
    color1 = ["gold", "gold", "darkorange", "gold", "dimgray", "darkorange", 
              "dimgray", "gold", "darkorange", "dimgray", "gold", "dimgray", 
              "darkorange", "dimgray", "dimgray", "yellowgreen"]

    generate_bar(True,  extract_dict(top_ten_data, "country"), 
                 extract_dict(top_ten_data, "medal_count"), 
                 6000, 75, color1 , 
                 "Medal Count of Countries", "Country", 
                 "Medal Count", "medal.png")
    
    # gdp graphs
    colors = ["darkgreen", "darkgreen", "yellowgreen", "darkgreen", "yellowgreen", 
              "darkorange", "darkred", "darkorange", "darkorange", "darkred"]
    
    generate_bar(True, listfinder(country_lis, top_5_index, low_5_index), 
                 listfinder(country_gdp, top_5_index, low_5_index), 
                 12, 75, colors, 
                 "Average Percent Change of Highest and Lowest Increases in GDP", 
                 "Country", "Average Percent Change", "gdp.png")
    
    
    # generate region maps
    # ---------------------
    # all olympics
    color2 = organize(country_gdp, 6, "darkred", 7, "darkorange", 9, "gold", 
                      11, "yellowgreen", "darkgreen", "dimgray")
    
    generate_region("Location of All Olympic Medals", True,
                    finder(all_medal_count, loc_data, 'country', 0, float, 1), 
                    finder(all_medal_count, loc_data, 'country', 0, float, 2), 
                    organize(extract_dict(all_medal_count, "medal_count"), 100, 
                             5, 1000, 15, 2500, 25, 6000, 40, 100, 0), 
                    color2, False, "allregion.pdf")
    
    # winter olympics
    
    generate_region("Location of Winter Olympic Medals", False,
                    finder(win_medal_count, loc_data, 'country', 0, float, 1), 
                    finder(win_medal_count, loc_data, 'country', 0, float, 2), 
                    organize(extract_dict(win_medal_count, "medal_count"), 100, 
                             5, 1000, 15, 2500, 25, 6000, 40, 100, 0), 
                    "mediumslateblue", False, "winterregion.pdf")
    
    # summer olympics
    generate_region("Location of Summer Olympic Medals", False,
                    finder(sum_medal_count, loc_data, 'country', 0, float, 1), 
                    finder(sum_medal_count, loc_data, 'country', 0, float, 2), 
                    organize(extract_dict(sum_medal_count, "medal_count"), 100, 
                             5, 1000, 15, 2500, 25, 6000, 40, 100, 0), 
                    "mediumslateblue", False, "summerregion.png")
    
    # Just Europe
    generate_region("Location of All European Olympic Medals", True,
                    finder(all_medal_count, loc_data, 'country', 0, float, 1), 
                    finder(all_medal_count, loc_data, 'country', 0, float, 2), 
                    organize(extract_dict(all_medal_count, "medal_count"), 100, 
                             15, 1000, 50, 2500, 150, 6000, 350, 500, 0), 
                    color2, True, "europe.png")
    
if __name__ == "__main__":    
    main()
    
    
    
"""
Dataset Citations:
--------------------
ATHLETE_FILE:
    Dataset was obtained with:
        https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results
    Note: dataset was updated to clarify country names, 
          team name column was replaced with the corresponding name of country,
          commas were replaces with spaces.

GDP_FILE:
    Dataset was obtained with:
        https://www.kaggle.com/datasets/rinichristy/countries-gdp-19602020
    Note: dataset was updated to remove commas from country names
    
LOCATION:
    Dataset was obtained with:
        https://www.kaggle.com/datasets/franckepeixoto/countries 
    Note: Additional countries were added to the dataset to represent 
    countries that no longer exist
    
"""