######################## BEGIN LICENSE BLOCK ########################
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
# 02110-1301  USA
######################### END LICENSE BLOCK #########################


# ----------------------------------- #
# pre-processing your features string #
# ----------------------------------- #
def stringPreprocessing(fea_string,
                        fea_split,            # What symbol split your features, like ',' or ',\n' ,etc.
                        if_delSpace = True,   # Do you want to remove spaces on both sides of the feature?
                        if_addComma = True,   # Do you want to add a ',' in the end of the line?
                        if_addEnter = True,   # Do you want to add a '\n' in the end of the line?
                        fea_intercept = [],   # Intercept the string between the two strings in each feature as a new feature, such as ['as ', ',']
                        ):
    fea_list = []

    # fea_intercept first
    if fea_intercept != []:

        if len(fea_intercept) != 2:
            return 'Error: you should put TWO elements in fea_intercept!'

        fea_string.split(fea_split)
        for item in fea_string:
            fea_list.append(item.split(fea_intercept[0])[1].split(fea_intercept[1])[0])

    else:
        fea_list = fea_string.split(fea_split)

    # remove space?
    if if_delSpace == True:
        for item in fea_list:
            item = item.strip()

    # add ',' ?
    if if_addComma == True:
        for i, item in enumerate(fea_list):
            if i < len(fea_list) - 1:
                item = item + ','

    # add '\n' ?
    if if_addEnter == True:
        for i, item in enumerate(fea_list):
            if i < len(fea_list) - 1:
                item = item + '\n'

    ret = ''
    for item in fea_list:
        ret += item

    return ret




# ----------------------------------- #
#  extract your features in a string  #
# ----------------------------------- #
def featuresExtractor(fea_string,
                      fea_split,    # What symbol split your features, like ',' or ',\n' ,etc.
                      keyword       # Features you want to extract which has this keyword
                     ):
    fea_list = fea_string.split(fea_split)
    ret = ''

    # Extractor
    for i, item in enumerate(fea_list):
        if keyword in item:
            ret += item
        if i < len(fea_list) - 1:
            ret = ret + ',\n'

    return ret