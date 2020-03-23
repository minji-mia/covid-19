#!/usr/bin/env python3
################################################################################
# Name:    dic.py
# Purpose: This Python 3 module defines utility dictionaries for fetch_data.py.
# Author:  Huidae Cho
# Since:   February 2, 2020
#
# Copyright (C) 2020, Huidae Cho <https://idea.isnew.info>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
################################################################################

en = {
    '安东': 'Andong',
    '安徽': 'Anhui',
    '察哈尔': 'Chahar',
    '福建': 'Fujian',
    '甘肃': 'Gansu',
    '广东': 'Guangdong',
    '广西': 'Guangxi',
    '贵州': 'Guizhou',
    '海南': 'Hainan',
    '河北': 'Hebei',
    '合江': 'Hejiang',
    '黑龙江': 'Heilongjiang',
    '河南': 'Henan',
    '湖北': 'Hubei',
    '湖南': 'Hunan',
    '江苏': 'Jiangsu',
    '江西': 'Jiangxi',
    '吉林': 'Jilin',
    '辽北': 'Liaobei',
    '辽东': 'Liaodong',
    '辽宁': 'Liaoning',
    '辽西': 'Liaoxi',
    '嫩江': 'Nenjiang',
    '宁夏': 'Ningxia',
    '牡丹江': 'Mudanjiang',
    '平原': 'Pingyuan',
    '青海': 'Qinghai',
    '热河': 'Rehe',
    '四川': 'Sichuan',
    '陕西': 'Shaanxi',
    '山东': 'Shandong',
    '山西': 'Shanxi',
    '松江': 'Songjiang',
    '绥远': 'Suiyuan',
    '台湾': 'Taiwan',
    '西康': 'Xikang',
    '兴安': "Xing'an",
    '新疆': 'Xinjiang',
    '云南': 'Yunnan',
    '浙江': 'Zhejiang',

    '广西': 'Guangxi',
    '内蒙古': 'Inner Mongolia',
    '宁夏': 'Ningxia',
    '西藏': 'Tibet',
    '新疆': 'Xinjiang',

    '鞍山': 'Anshan',
    '北京': 'Beijing',
    '本溪': 'Benxi',
    '长春': 'Changchun',
    '重庆': 'Chongqing',
    '大连': 'Dalian',
    '旅大': 'Lüda',
    '抚顺': 'Fushun',
    '广州': 'Guangzhou',
    '哈尔滨': 'Harbin',
    '南京': 'Nanjing',
    '上海': 'Shanghai',
    '沈阳': 'Shenyang',
    '天津': 'Tianjin',
    '汉口': 'Hankou',
    '武汉': 'Wuhan',
    '西安': "Xi'an",

    '香港': 'Hong Kong',
    '澳门': 'Macau',

    '서울': 'Seoul',
    '부산': 'Busan',
    '대구': 'Daegu',
    '인천': 'Incheon',
    '광주': 'Gwangju',
    '대전': 'Daejeon',
    '울산': 'Ulsan',
    '세종': 'Sejong',
    '경기': 'Gyeonggi',
    '강원': 'Gangwon',
    '충북': 'Chungbuk',
    '충남': 'Chungnam',
    '전북': 'Jeonbuk',
    '전남': 'Jeonnam',
    '경북': 'Gyeongbuk',
    '경남': 'Gyeongnam',
    '제주': 'Jeju',
    '검역': 'Quarantine',
}

us_states = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming',

    'AS': 'American Samoa',
    'DC': 'District of Columbia',
    'FM': 'Federated States of Micronesia',
    'GU': 'Guam',
    'MH': 'Marshall Islands',
    'MP': 'Northern Mariana Islands',
    'PW': 'Palau',
    'PR': 'Puerto Rico',
    'VI': 'Virgin Islands',
}

co_names = {
    'US': 'United States',
    'Republic of Korea': 'South Korea',
    'Korea, South': 'South Korea',
    'Iran (Islamic Republic of)': 'Iran',
    'Republic of Moldova': 'Moldova',
    'Taiwan*': 'Taiwan',
    'Bahamas, The': 'Bahamas',
    'The Bahamas': 'Bahamas',
    'Gambia, The': 'Gambia',
    'The Gambia': 'Gambia',
    'Congo (Brazzaville)': 'Congo Republic',
    'Congo (Kinshasa)': 'Congo Democratic Republic',
    'Czechia': 'Czech Republic',
}

keymap = {
    'US, United States': 'United States, United States',
    'Washington, D.C., United States': 'District of Columbia, United States',
    ', Puerto Rico': 'Puerto Rico, United States',
    ', Guam': 'Guam, United States',
    'United States Virgin Islands, United States': 'Virgin Islands, United States',

    ', France': 'France, France',
    ', Reunion': 'Reunion, France',
    ', Mayotte': 'Mayotte, France',
    ', French Guiana': 'French Guiana, France',
    ', Guadeloupe': 'Guadeloupe, France',
    ', Martinique': 'Martinique, France',
    'St Martin, France': 'Saint Martin, France',

    ', Netherlands': 'Netherlands, Netherlands',
    ', Aruba': 'Aruba, Netherlands',

    ', Denmark': 'Denmark, Denmark',
    ', Greenland': 'Greenland, Denmark',

    ', United Kingdom': 'United Kingdom, United Kingdom',
}

latlong = {
    ', Congo Republic': {'latitude': -0.2280, 'longitude': 15.8277},
    ', Congo Democratic Republic': {'latitude': -4.0383, 'longitude': 21.7587},
}
