{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: numpy in c:\\users\\ryans\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (1.26.1)\n",
      "Requirement already satisfied: pandas in c:\\users\\ryans\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (2.1.2)\n",
      "Requirement already satisfied: numpy<2,>=1.23.2 in c:\\users\\ryans\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from pandas) (1.26.1)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\ryans\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from pandas) (2.8.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\ryans\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from pandas) (2023.3.post1)\n",
      "Requirement already satisfied: tzdata>=2022.1 in c:\\users\\ryans\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from pandas) (2023.3)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\ryans\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n",
      "Requirement already satisfied: sklearn in c:\\users\\ryans\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (0.0.post11)\n"
     ]
    }
   ],
   "source": [
    "!pip install numpy\n",
    "!pip install pandas\n",
    "!pip install sklearn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 449,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import sklearn\n",
    "import pickle"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Setting Up Data Set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 450,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv('laptop_price.csv',encoding='latin_1')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Analysis ##"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 451,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>laptop_ID</th>\n",
       "      <th>Company</th>\n",
       "      <th>Product</th>\n",
       "      <th>TypeName</th>\n",
       "      <th>Inches</th>\n",
       "      <th>ScreenResolution</th>\n",
       "      <th>Cpu</th>\n",
       "      <th>Ram</th>\n",
       "      <th>Gpu</th>\n",
       "      <th>OpSys</th>\n",
       "      <th>Weight</th>\n",
       "      <th>Price_euros</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Apple</td>\n",
       "      <td>MacBook Pro</td>\n",
       "      <td>Ultrabook</td>\n",
       "      <td>13.3</td>\n",
       "      <td>IPS Panel Retina Display 2560x1600</td>\n",
       "      <td>Intel Core i5 2.3GHz</td>\n",
       "      <td>8GB</td>\n",
       "      <td>Intel Iris Plus Graphics 640</td>\n",
       "      <td>macOS</td>\n",
       "      <td>1.37kg</td>\n",
       "      <td>1339.69</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Apple</td>\n",
       "      <td>Macbook Air</td>\n",
       "      <td>Ultrabook</td>\n",
       "      <td>13.3</td>\n",
       "      <td>1440x900</td>\n",
       "      <td>Intel Core i5 1.8GHz</td>\n",
       "      <td>8GB</td>\n",
       "      <td>Intel HD Graphics 6000</td>\n",
       "      <td>macOS</td>\n",
       "      <td>1.34kg</td>\n",
       "      <td>898.94</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>HP</td>\n",
       "      <td>250 G6</td>\n",
       "      <td>Notebook</td>\n",
       "      <td>15.6</td>\n",
       "      <td>Full HD 1920x1080</td>\n",
       "      <td>Intel Core i5 7200U 2.5GHz</td>\n",
       "      <td>8GB</td>\n",
       "      <td>Intel HD Graphics 620</td>\n",
       "      <td>No OS</td>\n",
       "      <td>1.86kg</td>\n",
       "      <td>575.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Apple</td>\n",
       "      <td>MacBook Pro</td>\n",
       "      <td>Ultrabook</td>\n",
       "      <td>15.4</td>\n",
       "      <td>IPS Panel Retina Display 2880x1800</td>\n",
       "      <td>Intel Core i7 2.7GHz</td>\n",
       "      <td>16GB</td>\n",
       "      <td>AMD Radeon Pro 455</td>\n",
       "      <td>macOS</td>\n",
       "      <td>1.83kg</td>\n",
       "      <td>2537.45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Apple</td>\n",
       "      <td>MacBook Pro</td>\n",
       "      <td>Ultrabook</td>\n",
       "      <td>13.3</td>\n",
       "      <td>IPS Panel Retina Display 2560x1600</td>\n",
       "      <td>Intel Core i5 3.1GHz</td>\n",
       "      <td>8GB</td>\n",
       "      <td>Intel Iris Plus Graphics 650</td>\n",
       "      <td>macOS</td>\n",
       "      <td>1.37kg</td>\n",
       "      <td>1803.60</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   laptop_ID Company      Product   TypeName  Inches  \\\n",
       "0          1   Apple  MacBook Pro  Ultrabook    13.3   \n",
       "1          2   Apple  Macbook Air  Ultrabook    13.3   \n",
       "2          3      HP       250 G6   Notebook    15.6   \n",
       "3          4   Apple  MacBook Pro  Ultrabook    15.4   \n",
       "4          5   Apple  MacBook Pro  Ultrabook    13.3   \n",
       "\n",
       "                     ScreenResolution                         Cpu   Ram  \\\n",
       "0  IPS Panel Retina Display 2560x1600        Intel Core i5 2.3GHz   8GB   \n",
       "1                            1440x900        Intel Core i5 1.8GHz   8GB   \n",
       "2                   Full HD 1920x1080  Intel Core i5 7200U 2.5GHz   8GB   \n",
       "3  IPS Panel Retina Display 2880x1800        Intel Core i7 2.7GHz  16GB   \n",
       "4  IPS Panel Retina Display 2560x1600        Intel Core i5 3.1GHz   8GB   \n",
       "\n",
       "                            Gpu  OpSys  Weight  Price_euros  \n",
       "0  Intel Iris Plus Graphics 640  macOS  1.37kg      1339.69  \n",
       "1        Intel HD Graphics 6000  macOS  1.34kg       898.94  \n",
       "2         Intel HD Graphics 620  No OS  1.86kg       575.00  \n",
       "3            AMD Radeon Pro 455  macOS  1.83kg      2537.45  \n",
       "4  Intel Iris Plus Graphics 650  macOS  1.37kg      1803.60  "
      ]
     },
     "execution_count": 451,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()  #Outputs the head of data set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 452,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "laptop_ID           0\n",
       "Company             0\n",
       "Product             0\n",
       "TypeName            0\n",
       "Inches              0\n",
       "ScreenResolution    0\n",
       "Cpu                 0\n",
       "Ram                 0\n",
       "Gpu                 0\n",
       "OpSys               0\n",
       "Weight              0\n",
       "Price_euros         0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 452,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum() #Outputs the sum of data per column which are null"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 453,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1303 entries, 0 to 1302\n",
      "Data columns (total 12 columns):\n",
      " #   Column            Non-Null Count  Dtype  \n",
      "---  ------            --------------  -----  \n",
      " 0   laptop_ID         1303 non-null   int64  \n",
      " 1   Company           1303 non-null   object \n",
      " 2   Product           1303 non-null   object \n",
      " 3   TypeName          1303 non-null   object \n",
      " 4   Inches            1303 non-null   float64\n",
      " 5   ScreenResolution  1303 non-null   object \n",
      " 6   Cpu               1303 non-null   object \n",
      " 7   Ram               1303 non-null   object \n",
      " 8   Gpu               1303 non-null   object \n",
      " 9   OpSys             1303 non-null   object \n",
      " 10  Weight            1303 non-null   object \n",
      " 11  Price_euros       1303 non-null   float64\n",
      "dtypes: float64(2), int64(1), object(9)\n",
      "memory usage: 122.3+ KB\n"
     ]
    }
   ],
   "source": [
    "data.info() #Column Names , Data Types and Detials"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Both Ram and Weight Columns Should Be Converted To Numerics ##"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 454,
   "metadata": {},
   "outputs": [],
   "source": [
    "data['Ram'] = data['Ram'].str.replace('GB','').astype('int32')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 455,
   "metadata": {},
   "outputs": [],
   "source": [
    "data['Weight'] = data['Weight'].str.replace('kg','').astype('float32')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 456,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>laptop_ID</th>\n",
       "      <th>Company</th>\n",
       "      <th>Product</th>\n",
       "      <th>TypeName</th>\n",
       "      <th>Inches</th>\n",
       "      <th>ScreenResolution</th>\n",
       "      <th>Cpu</th>\n",
       "      <th>Ram</th>\n",
       "      <th>Gpu</th>\n",
       "      <th>OpSys</th>\n",
       "      <th>Weight</th>\n",
       "      <th>Price_euros</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Apple</td>\n",
       "      <td>MacBook Pro</td>\n",
       "      <td>Ultrabook</td>\n",
       "      <td>13.3</td>\n",
       "      <td>IPS Panel Retina Display 2560x1600</td>\n",
       "      <td>Intel Core i5 2.3GHz</td>\n",
       "      <td>8</td>\n",
       "      <td>Intel Iris Plus Graphics 640</td>\n",
       "      <td>macOS</td>\n",
       "      <td>1.37</td>\n",
       "      <td>1339.69</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Apple</td>\n",
       "      <td>Macbook Air</td>\n",
       "      <td>Ultrabook</td>\n",
       "      <td>13.3</td>\n",
       "      <td>1440x900</td>\n",
       "      <td>Intel Core i5 1.8GHz</td>\n",
       "      <td>8</td>\n",
       "      <td>Intel HD Graphics 6000</td>\n",
       "      <td>macOS</td>\n",
       "      <td>1.34</td>\n",
       "      <td>898.94</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>HP</td>\n",
       "      <td>250 G6</td>\n",
       "      <td>Notebook</td>\n",
       "      <td>15.6</td>\n",
       "      <td>Full HD 1920x1080</td>\n",
       "      <td>Intel Core i5 7200U 2.5GHz</td>\n",
       "      <td>8</td>\n",
       "      <td>Intel HD Graphics 620</td>\n",
       "      <td>No OS</td>\n",
       "      <td>1.86</td>\n",
       "      <td>575.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Apple</td>\n",
       "      <td>MacBook Pro</td>\n",
       "      <td>Ultrabook</td>\n",
       "      <td>15.4</td>\n",
       "      <td>IPS Panel Retina Display 2880x1800</td>\n",
       "      <td>Intel Core i7 2.7GHz</td>\n",
       "      <td>16</td>\n",
       "      <td>AMD Radeon Pro 455</td>\n",
       "      <td>macOS</td>\n",
       "      <td>1.83</td>\n",
       "      <td>2537.45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Apple</td>\n",
       "      <td>MacBook Pro</td>\n",
       "      <td>Ultrabook</td>\n",
       "      <td>13.3</td>\n",
       "      <td>IPS Panel Retina Display 2560x1600</td>\n",
       "      <td>Intel Core i5 3.1GHz</td>\n",
       "      <td>8</td>\n",
       "      <td>Intel Iris Plus Graphics 650</td>\n",
       "      <td>macOS</td>\n",
       "      <td>1.37</td>\n",
       "      <td>1803.60</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   laptop_ID Company      Product   TypeName  Inches  \\\n",
       "0          1   Apple  MacBook Pro  Ultrabook    13.3   \n",
       "1          2   Apple  Macbook Air  Ultrabook    13.3   \n",
       "2          3      HP       250 G6   Notebook    15.6   \n",
       "3          4   Apple  MacBook Pro  Ultrabook    15.4   \n",
       "4          5   Apple  MacBook Pro  Ultrabook    13.3   \n",
       "\n",
       "                     ScreenResolution                         Cpu  Ram  \\\n",
       "0  IPS Panel Retina Display 2560x1600        Intel Core i5 2.3GHz    8   \n",
       "1                            1440x900        Intel Core i5 1.8GHz    8   \n",
       "2                   Full HD 1920x1080  Intel Core i5 7200U 2.5GHz    8   \n",
       "3  IPS Panel Retina Display 2880x1800        Intel Core i7 2.7GHz   16   \n",
       "4  IPS Panel Retina Display 2560x1600        Intel Core i5 3.1GHz    8   \n",
       "\n",
       "                            Gpu  OpSys  Weight  Price_euros  \n",
       "0  Intel Iris Plus Graphics 640  macOS    1.37      1339.69  \n",
       "1        Intel HD Graphics 6000  macOS    1.34       898.94  \n",
       "2         Intel HD Graphics 620  No OS    1.86       575.00  \n",
       "3            AMD Radeon Pro 455  macOS    1.83      2537.45  \n",
       "4  Intel Iris Plus Graphics 650  macOS    1.37      1803.60  "
      ]
     },
     "execution_count": 456,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head() #to check the conversions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 457,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1303 entries, 0 to 1302\n",
      "Data columns (total 12 columns):\n",
      " #   Column            Non-Null Count  Dtype  \n",
      "---  ------            --------------  -----  \n",
      " 0   laptop_ID         1303 non-null   int64  \n",
      " 1   Company           1303 non-null   object \n",
      " 2   Product           1303 non-null   object \n",
      " 3   TypeName          1303 non-null   object \n",
      " 4   Inches            1303 non-null   float64\n",
      " 5   ScreenResolution  1303 non-null   object \n",
      " 6   Cpu               1303 non-null   object \n",
      " 7   Ram               1303 non-null   int32  \n",
      " 8   Gpu               1303 non-null   object \n",
      " 9   OpSys             1303 non-null   object \n",
      " 10  Weight            1303 non-null   float32\n",
      " 11  Price_euros       1303 non-null   float64\n",
      "dtypes: float32(1), float64(2), int32(1), int64(1), object(7)\n",
      "memory usage: 112.1+ KB\n"
     ]
    }
   ],
   "source": [
    "data.info()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 458,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1303, 12)"
      ]
     },
     "execution_count": 458,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Which Data Effects The Price More\n",
    "\n",
    "data.corr()['Price_euros']\n",
    "laptop_ID      0.067830\n",
    "Inches         0.068197\n",
    "Ram            0.743007\n",
    "Weight         0.210370\n",
    "Price_euros    1.000000\n",
    "Name: Price_euros, dtype: float64"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Removing Categories With Too Many Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 459,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Company\n",
       "Dell         297\n",
       "Lenovo       297\n",
       "HP           274\n",
       "Asus         158\n",
       "Acer         103\n",
       "MSI           54\n",
       "Toshiba       48\n",
       "Apple         21\n",
       "Samsung        9\n",
       "Razer          7\n",
       "Mediacom       7\n",
       "Microsoft      6\n",
       "Xiaomi         4\n",
       "Vero           4\n",
       "Chuwi          3\n",
       "Google         3\n",
       "Fujitsu        3\n",
       "LG             3\n",
       "Huawei         2\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 459,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Company'].value_counts() # Can Get The Category Counts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 460,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "19"
      ]
     },
     "execution_count": 460,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(data['Company'].value_counts()) #Number Of Categories"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 492,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Function to Remove Selected Categories From Data\n",
    "def add_company(inpt):\n",
    "    if inpt == 'Samsung' or inpt == 'Razer' or inpt == 'Mediacom' or inpt == 'Microsoft'or inpt == 'Xiaomi'or inpt == 'Vero'or inpt == 'Chuwi'or inpt == 'Google'or inpt == 'Fujitsu'or inpt == 'LG'or inpt == 'Huawei':\n",
    "        return 'Other'\n",
    "    else:\n",
    "        return inpt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 493,
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'Company'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "File \u001b[1;32mc:\\Users\\ryans\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\pandas\\core\\indexes\\base.py:3790\u001b[0m, in \u001b[0;36mIndex.get_loc\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m   3789\u001b[0m \u001b[39mtry\u001b[39;00m:\n\u001b[1;32m-> 3790\u001b[0m     \u001b[39mreturn\u001b[39;00m \u001b[39mself\u001b[39;49m\u001b[39m.\u001b[39;49m_engine\u001b[39m.\u001b[39;49mget_loc(casted_key)\n\u001b[0;32m   3791\u001b[0m \u001b[39mexcept\u001b[39;00m \u001b[39mKeyError\u001b[39;00m \u001b[39mas\u001b[39;00m err:\n",
      "File \u001b[1;32mindex.pyx:152\u001b[0m, in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[1;34m()\u001b[0m\n",
      "File \u001b[1;32mindex.pyx:181\u001b[0m, in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[1;34m()\u001b[0m\n",
      "File \u001b[1;32mpandas\\_libs\\hashtable_class_helper.pxi:7080\u001b[0m, in \u001b[0;36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[1;34m()\u001b[0m\n",
      "File \u001b[1;32mpandas\\_libs\\hashtable_class_helper.pxi:7088\u001b[0m, in \u001b[0;36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;31mKeyError\u001b[0m: 'Company'",
      "\nThe above exception was the direct cause of the following exception:\n",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32mc:\\Users\\ryans\\Desktop\\Laptop Price Predictor\\model\\.ipynb_checkpoints\\model_building.ipynb Cell 20\u001b[0m line \u001b[0;36m1\n\u001b[1;32m----> <a href='vscode-notebook-cell:/c%3A/Users/ryans/Desktop/Laptop%20Price%20Predictor/model/.ipynb_checkpoints/model_building.ipynb#X25sZmlsZQ%3D%3D?line=0'>1</a>\u001b[0m \u001b[39mlen\u001b[39m(data[\u001b[39m'\u001b[39;49m\u001b[39mCompany\u001b[39;49m\u001b[39m'\u001b[39;49m]\u001b[39m.\u001b[39mvalue_counts()) \u001b[39m# Can See the that selected categories are removed\u001b[39;00m\n",
      "File \u001b[1;32mc:\\Users\\ryans\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\pandas\\core\\frame.py:3893\u001b[0m, in \u001b[0;36mDataFrame.__getitem__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m   3891\u001b[0m \u001b[39mif\u001b[39;00m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mcolumns\u001b[39m.\u001b[39mnlevels \u001b[39m>\u001b[39m \u001b[39m1\u001b[39m:\n\u001b[0;32m   3892\u001b[0m     \u001b[39mreturn\u001b[39;00m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39m_getitem_multilevel(key)\n\u001b[1;32m-> 3893\u001b[0m indexer \u001b[39m=\u001b[39m \u001b[39mself\u001b[39;49m\u001b[39m.\u001b[39;49mcolumns\u001b[39m.\u001b[39;49mget_loc(key)\n\u001b[0;32m   3894\u001b[0m \u001b[39mif\u001b[39;00m is_integer(indexer):\n\u001b[0;32m   3895\u001b[0m     indexer \u001b[39m=\u001b[39m [indexer]\n",
      "File \u001b[1;32mc:\\Users\\ryans\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\pandas\\core\\indexes\\base.py:3797\u001b[0m, in \u001b[0;36mIndex.get_loc\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m   3792\u001b[0m     \u001b[39mif\u001b[39;00m \u001b[39misinstance\u001b[39m(casted_key, \u001b[39mslice\u001b[39m) \u001b[39mor\u001b[39;00m (\n\u001b[0;32m   3793\u001b[0m         \u001b[39misinstance\u001b[39m(casted_key, abc\u001b[39m.\u001b[39mIterable)\n\u001b[0;32m   3794\u001b[0m         \u001b[39mand\u001b[39;00m \u001b[39many\u001b[39m(\u001b[39misinstance\u001b[39m(x, \u001b[39mslice\u001b[39m) \u001b[39mfor\u001b[39;00m x \u001b[39min\u001b[39;00m casted_key)\n\u001b[0;32m   3795\u001b[0m     ):\n\u001b[0;32m   3796\u001b[0m         \u001b[39mraise\u001b[39;00m InvalidIndexError(key)\n\u001b[1;32m-> 3797\u001b[0m     \u001b[39mraise\u001b[39;00m \u001b[39mKeyError\u001b[39;00m(key) \u001b[39mfrom\u001b[39;00m \u001b[39merr\u001b[39;00m\n\u001b[0;32m   3798\u001b[0m \u001b[39mexcept\u001b[39;00m \u001b[39mTypeError\u001b[39;00m:\n\u001b[0;32m   3799\u001b[0m     \u001b[39m# If we have a listlike key, _check_indexing_error will raise\u001b[39;00m\n\u001b[0;32m   3800\u001b[0m     \u001b[39m#  InvalidIndexError. Otherwise we fall through and re-raise\u001b[39;00m\n\u001b[0;32m   3801\u001b[0m     \u001b[39m#  the TypeError.\u001b[39;00m\n\u001b[0;32m   3802\u001b[0m     \u001b[39mself\u001b[39m\u001b[39m.\u001b[39m_check_indexing_error(key)\n",
      "\u001b[1;31mKeyError\u001b[0m: 'Company'"
     ]
    }
   ],
   "source": [
    "len(data['Company'].value_counts()) # Can See the that selected categories are removed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 463,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "618"
      ]
     },
     "execution_count": 463,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(data['Product'].value_counts()) # Too much again"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 464,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "ScreenResolution\n",
       "Full HD 1920x1080                                507\n",
       "1366x768                                         281\n",
       "IPS Panel Full HD 1920x1080                      230\n",
       "IPS Panel Full HD / Touchscreen 1920x1080         53\n",
       "Full HD / Touchscreen 1920x1080                   47\n",
       "1600x900                                          23\n",
       "Touchscreen 1366x768                              16\n",
       "Quad HD+ / Touchscreen 3200x1800                  15\n",
       "IPS Panel 4K Ultra HD 3840x2160                   12\n",
       "IPS Panel 4K Ultra HD / Touchscreen 3840x2160     11\n",
       "4K Ultra HD / Touchscreen 3840x2160               10\n",
       "4K Ultra HD 3840x2160                              7\n",
       "Touchscreen 2560x1440                              7\n",
       "IPS Panel 1366x768                                 7\n",
       "IPS Panel Quad HD+ / Touchscreen 3200x1800         6\n",
       "IPS Panel Retina Display 2560x1600                 6\n",
       "IPS Panel Retina Display 2304x1440                 6\n",
       "Touchscreen 2256x1504                              6\n",
       "IPS Panel Touchscreen 2560x1440                    5\n",
       "IPS Panel Retina Display 2880x1800                 4\n",
       "IPS Panel Touchscreen 1920x1200                    4\n",
       "1440x900                                           4\n",
       "IPS Panel 2560x1440                                4\n",
       "IPS Panel Quad HD+ 2560x1440                       3\n",
       "Quad HD+ 3200x1800                                 3\n",
       "1920x1080                                          3\n",
       "Touchscreen 2400x1600                              3\n",
       "2560x1440                                          3\n",
       "IPS Panel Touchscreen 1366x768                     3\n",
       "IPS Panel Touchscreen / 4K Ultra HD 3840x2160      2\n",
       "IPS Panel Full HD 2160x1440                        2\n",
       "IPS Panel Quad HD+ 3200x1800                       2\n",
       "IPS Panel Retina Display 2736x1824                 1\n",
       "IPS Panel Full HD 1920x1200                        1\n",
       "IPS Panel Full HD 2560x1440                        1\n",
       "IPS Panel Full HD 1366x768                         1\n",
       "Touchscreen / Full HD 1920x1080                    1\n",
       "Touchscreen / Quad HD+ 3200x1800                   1\n",
       "Touchscreen / 4K Ultra HD 3840x2160                1\n",
       "IPS Panel Touchscreen 2400x1600                    1\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 464,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['ScreenResolution'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 465,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Here Selected Some Main Technologies which can effect the price of an Laptop\n",
    "\n",
    "data['Touchscreen'] = data['ScreenResolution'].apply(lambda x:1 if 'Touchscreen' in x else 0)\n",
    "data['Ips'] = data['ScreenResolution'].apply(lambda x:1 if 'IPS' in x else 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 466,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Cpu\n",
       "Intel Core i5 7200U 2.5GHz       190\n",
       "Intel Core i7 7700HQ 2.8GHz      146\n",
       "Intel Core i7 7500U 2.7GHz       134\n",
       "Intel Core i7 8550U 1.8GHz        73\n",
       "Intel Core i5 8250U 1.6GHz        72\n",
       "                                ... \n",
       "Intel Core M M3-6Y30 0.9GHz        1\n",
       "AMD A9-Series 9420 2.9GHz          1\n",
       "Intel Core i3 6006U 2.2GHz         1\n",
       "AMD A6-Series 7310 2GHz            1\n",
       "Intel Xeon E3-1535M v6 3.1GHz      1\n",
       "Name: count, Length: 118, dtype: int64"
      ]
     },
     "execution_count": 466,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Cpu'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 467,
   "metadata": {},
   "outputs": [],
   "source": [
    "data['cpu_name'] = data['Cpu'].apply(lambda x:\" \".join(x.split()[0:3])) #Takes Only The First 3 Words"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 468,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Function to put \n",
    "def set_processor(name):\n",
    "    if name == 'Intel Core i7' or name == 'Intel Core i5' or name == 'Intel Core i3':\n",
    "        return name\n",
    "    else:\n",
    "        if name.split()[0] == 'AMD':\n",
    "            return 'AMD'\n",
    "        else:\n",
    "            return 'Other'\n",
    "        \n",
    "data['cpu_name'] = data['cpu_name'].apply(set_processor)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 469,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "cpu_name\n",
       "Intel Core i7    527\n",
       "Intel Core i5    423\n",
       "Other            155\n",
       "Intel Core i3    136\n",
       "AMD               62\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 469,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['cpu_name'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 470,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Ram\n",
       "8     619\n",
       "4     375\n",
       "16    200\n",
       "6      41\n",
       "12     25\n",
       "2      22\n",
       "32     17\n",
       "24      3\n",
       "64      1\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 470,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Ram'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 471,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Gpu\n",
       "Intel HD Graphics 620      281\n",
       "Intel HD Graphics 520      185\n",
       "Intel UHD Graphics 620      68\n",
       "Nvidia GeForce GTX 1050     66\n",
       "Nvidia GeForce GTX 1060     48\n",
       "                          ... \n",
       "AMD Radeon R5 520            1\n",
       "AMD Radeon R7                1\n",
       "Intel HD Graphics 540        1\n",
       "AMD Radeon 540               1\n",
       "ARM Mali T860 MP4            1\n",
       "Name: count, Length: 110, dtype: int64"
      ]
     },
     "execution_count": 471,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Gpu'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 472,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Takes Only The First Value\n",
    "data['gpu_name'] = data['Gpu'].apply(lambda x:\" \".join(x.split()[0:1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 473,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "gpu_name\n",
       "Intel     722\n",
       "Nvidia    400\n",
       "AMD       180\n",
       "ARM         1\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 473,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['gpu_name'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 474,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Removes ARM Category\n",
    "data = data[data['gpu_name'] != 'ARM']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 475,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "OpSys\n",
       "Windows 10      1072\n",
       "No OS             66\n",
       "Linux             62\n",
       "Windows 7         45\n",
       "Chrome OS         26\n",
       "macOS             13\n",
       "Mac OS X           8\n",
       "Windows 10 S       8\n",
       "Android            2\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 475,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['OpSys'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 476,
   "metadata": {},
   "outputs": [],
   "source": [
    "def set_os(inpt):\n",
    "    if inpt == 'Windows 10' or inpt == 'Windows 7' or inpt == 'Windows 10 S':\n",
    "        return 'Windows'\n",
    "    elif inpt == 'macOS' or inpt == 'Mac OS X':\n",
    "        return 'Mac'\n",
    "    elif inpt == 'Linux':\n",
    "        return inpt\n",
    "    else:\n",
    "        return 'Other'\n",
    "    \n",
    "data['OpSys'] = data['OpSys'].apply(set_os)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 477,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "OpSys\n",
       "Windows    1125\n",
       "Other        94\n",
       "Linux        62\n",
       "Mac          21\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 477,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['OpSys'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 478,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Dropping Unwanted Columns\n",
    "data = data.drop(columns=['laptop_ID', 'Inches', 'Product', 'ScreenResolution', 'Cpu', 'Gpu'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 479,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Company</th>\n",
       "      <th>TypeName</th>\n",
       "      <th>Ram</th>\n",
       "      <th>OpSys</th>\n",
       "      <th>Weight</th>\n",
       "      <th>Price_euros</th>\n",
       "      <th>Touchscreen</th>\n",
       "      <th>Ips</th>\n",
       "      <th>cpu_name</th>\n",
       "      <th>gpu_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Apple</td>\n",
       "      <td>Ultrabook</td>\n",
       "      <td>8</td>\n",
       "      <td>Mac</td>\n",
       "      <td>1.37</td>\n",
       "      <td>1339.69</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Intel Core i5</td>\n",
       "      <td>Intel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Apple</td>\n",
       "      <td>Ultrabook</td>\n",
       "      <td>8</td>\n",
       "      <td>Mac</td>\n",
       "      <td>1.34</td>\n",
       "      <td>898.94</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Intel Core i5</td>\n",
       "      <td>Intel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>HP</td>\n",
       "      <td>Notebook</td>\n",
       "      <td>8</td>\n",
       "      <td>Other</td>\n",
       "      <td>1.86</td>\n",
       "      <td>575.00</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Intel Core i5</td>\n",
       "      <td>Intel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Apple</td>\n",
       "      <td>Ultrabook</td>\n",
       "      <td>16</td>\n",
       "      <td>Mac</td>\n",
       "      <td>1.83</td>\n",
       "      <td>2537.45</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Intel Core i7</td>\n",
       "      <td>AMD</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Apple</td>\n",
       "      <td>Ultrabook</td>\n",
       "      <td>8</td>\n",
       "      <td>Mac</td>\n",
       "      <td>1.37</td>\n",
       "      <td>1803.60</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Intel Core i5</td>\n",
       "      <td>Intel</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Company   TypeName  Ram  OpSys  Weight  Price_euros  Touchscreen  Ips  \\\n",
       "0   Apple  Ultrabook    8    Mac    1.37      1339.69            0    1   \n",
       "1   Apple  Ultrabook    8    Mac    1.34       898.94            0    0   \n",
       "2      HP   Notebook    8  Other    1.86       575.00            0    0   \n",
       "3   Apple  Ultrabook   16    Mac    1.83      2537.45            0    1   \n",
       "4   Apple  Ultrabook    8    Mac    1.37      1803.60            0    1   \n",
       "\n",
       "        cpu_name gpu_name  \n",
       "0  Intel Core i5    Intel  \n",
       "1  Intel Core i5    Intel  \n",
       "2  Intel Core i5    Intel  \n",
       "3  Intel Core i7      AMD  \n",
       "4  Intel Core i5    Intel  "
      ]
     },
     "execution_count": 479,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Converting All These Data To Numerics  ##"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 480,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.get_dummies(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 481,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Ram</th>\n",
       "      <th>Weight</th>\n",
       "      <th>Price_euros</th>\n",
       "      <th>Touchscreen</th>\n",
       "      <th>Ips</th>\n",
       "      <th>Company_Acer</th>\n",
       "      <th>Company_Apple</th>\n",
       "      <th>Company_Asus</th>\n",
       "      <th>Company_Chuwi</th>\n",
       "      <th>Company_Dell</th>\n",
       "      <th>...</th>\n",
       "      <th>OpSys_Other</th>\n",
       "      <th>OpSys_Windows</th>\n",
       "      <th>cpu_name_AMD</th>\n",
       "      <th>cpu_name_Intel Core i3</th>\n",
       "      <th>cpu_name_Intel Core i5</th>\n",
       "      <th>cpu_name_Intel Core i7</th>\n",
       "      <th>cpu_name_Other</th>\n",
       "      <th>gpu_name_AMD</th>\n",
       "      <th>gpu_name_Intel</th>\n",
       "      <th>gpu_name_Nvidia</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>8</td>\n",
       "      <td>1.37</td>\n",
       "      <td>1339.69</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>...</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>8</td>\n",
       "      <td>1.34</td>\n",
       "      <td>898.94</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>...</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>8</td>\n",
       "      <td>1.86</td>\n",
       "      <td>575.00</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>...</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>16</td>\n",
       "      <td>1.83</td>\n",
       "      <td>2537.45</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>...</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>8</td>\n",
       "      <td>1.37</td>\n",
       "      <td>1803.60</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>...</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 42 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   Ram  Weight  Price_euros  Touchscreen  Ips  Company_Acer  Company_Apple  \\\n",
       "0    8    1.37      1339.69            0    1         False           True   \n",
       "1    8    1.34       898.94            0    0         False           True   \n",
       "2    8    1.86       575.00            0    0         False          False   \n",
       "3   16    1.83      2537.45            0    1         False           True   \n",
       "4    8    1.37      1803.60            0    1         False           True   \n",
       "\n",
       "   Company_Asus  Company_Chuwi  Company_Dell  ...  OpSys_Other  OpSys_Windows  \\\n",
       "0         False          False         False  ...        False          False   \n",
       "1         False          False         False  ...        False          False   \n",
       "2         False          False         False  ...         True          False   \n",
       "3         False          False         False  ...        False          False   \n",
       "4         False          False         False  ...        False          False   \n",
       "\n",
       "   cpu_name_AMD  cpu_name_Intel Core i3  cpu_name_Intel Core i5  \\\n",
       "0         False                   False                    True   \n",
       "1         False                   False                    True   \n",
       "2         False                   False                    True   \n",
       "3         False                   False                   False   \n",
       "4         False                   False                    True   \n",
       "\n",
       "   cpu_name_Intel Core i7  cpu_name_Other  gpu_name_AMD  gpu_name_Intel  \\\n",
       "0                   False           False         False            True   \n",
       "1                   False           False         False            True   \n",
       "2                   False           False         False            True   \n",
       "3                    True           False          True           False   \n",
       "4                   False           False         False            True   \n",
       "\n",
       "   gpu_name_Nvidia  \n",
       "0            False  \n",
       "1            False  \n",
       "2            False  \n",
       "3            False  \n",
       "4            False  \n",
       "\n",
       "[5 rows x 42 columns]"
      ]
     },
     "execution_count": 481,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Model Building and Selection ##"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 482,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = data.drop('Price_euros', axis=1) #Dropping Price Since now we are the ones who need to predict the price\n",
    "y = data['Price_euros'] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 483,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 484,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Model Traning\n",
    "def model_acc(model):\n",
    "    model.fit(X_train, y_train)\n",
    "    acc = model.score(X_test, y_test)\n",
    "    print(str(model)+ ' --> ' +str(acc))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 485,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LinearRegression() --> 0.6902511011690913\n",
      "Lasso() --> 0.6733797404522863\n",
      "DecisionTreeRegressor() --> 0.5711305714293251\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "RandomForestRegressor() --> 0.7073745481355154\n"
     ]
    }
   ],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "lr = LinearRegression()\n",
    "model_acc(lr)\n",
    "\n",
    "from sklearn.linear_model import Lasso\n",
    "lasso = Lasso()\n",
    "model_acc(lasso)\n",
    "\n",
    "from sklearn.tree import DecisionTreeRegressor\n",
    "dt = DecisionTreeRegressor()\n",
    "model_acc(dt)\n",
    "\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "rf = RandomForestRegressor()\n",
    "model_acc(rf)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 486,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Selects Random Forest Regressor Since Provides The Best Rate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 487,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7093949669174379"
      ]
     },
     "execution_count": 487,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.model_selection import GridSearchCV\n",
    "\n",
    "parameters = {'n_estimators':[10, 50, 100],\n",
    "              'criterion':['squared_error','absolute_error','poisson']}\n",
    "\n",
    "grid_obj = GridSearchCV(estimator=rf, param_grid=parameters)\n",
    "\n",
    "grid_fit = grid_obj.fit(X_train, y_train)\n",
    "\n",
    "best_model = grid_fit.best_estimator_\n",
    "\n",
    "best_model.score(X_test, y_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Saving ML Algorithm as a Pickle ##"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 488,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Ram', 'Weight', 'Touchscreen', 'Ips', 'Company_Acer', 'Company_Apple',\n",
       "       'Company_Asus', 'Company_Chuwi', 'Company_Dell', 'Company_Fujitsu',\n",
       "       'Company_Google', 'Company_HP', 'Company_Huawei', 'Company_LG',\n",
       "       'Company_Lenovo', 'Company_MSI', 'Company_Mediacom',\n",
       "       'Company_Microsoft', 'Company_Razer', 'Company_Samsung',\n",
       "       'Company_Toshiba', 'Company_Vero', 'Company_Xiaomi',\n",
       "       'TypeName_2 in 1 Convertible', 'TypeName_Gaming', 'TypeName_Netbook',\n",
       "       'TypeName_Notebook', 'TypeName_Ultrabook', 'TypeName_Workstation',\n",
       "       'OpSys_Linux', 'OpSys_Mac', 'OpSys_Other', 'OpSys_Windows',\n",
       "       'cpu_name_AMD', 'cpu_name_Intel Core i3', 'cpu_name_Intel Core i5',\n",
       "       'cpu_name_Intel Core i7', 'cpu_name_Other', 'gpu_name_AMD',\n",
       "       'gpu_name_Intel', 'gpu_name_Nvidia'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 488,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_test.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 489,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('predictor.pickle', 'wb') as file:\n",
    "    pickle.dump(best_model, file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 491,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\Users\\ryans\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\base.py:465: UserWarning: X does not have valid feature names, but RandomForestRegressor was fitted with feature names\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "X has 31 features, but RandomForestRegressor is expecting 41 features as input.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32mc:\\Users\\ryans\\Desktop\\Laptop Price Predictor\\model\\.ipynb_checkpoints\\model_building.ipynb Cell 51\u001b[0m line \u001b[0;36m1\n\u001b[1;32m----> <a href='vscode-notebook-cell:/c%3A/Users/ryans/Desktop/Laptop%20Price%20Predictor/model/.ipynb_checkpoints/model_building.ipynb#Y104sZmlsZQ%3D%3D?line=0'>1</a>\u001b[0m pred_value \u001b[39m=\u001b[39m best_model\u001b[39m.\u001b[39;49mpredict([[\u001b[39m8\u001b[39;49m, \u001b[39m1.3\u001b[39;49m, \u001b[39m1\u001b[39;49m, \u001b[39m1\u001b[39;49m, \u001b[39m0\u001b[39;49m, \u001b[39m1\u001b[39;49m, \u001b[39m0\u001b[39;49m, \u001b[39m1\u001b[39;49m, \u001b[39m0\u001b[39;49m, \u001b[39m0\u001b[39;49m, \u001b[39m0\u001b[39;49m, \u001b[39m0\u001b[39;49m, \u001b[39m0\u001b[39;49m, \u001b[39m0\u001b[39;49m, \u001b[39m0\u001b[39;49m, \u001b[39m1\u001b[39;49m, \u001b[39m0\u001b[39;49m, \u001b[39m0\u001b[39;49m, \u001b[39m1\u001b[39;49m, \u001b[39m0\u001b[39;49m, \u001b[39m0\u001b[39;49m, \u001b[39m1\u001b[39;49m, \u001b[39m0\u001b[39;49m, \u001b[39m0\u001b[39;49m, \u001b[39m0\u001b[39;49m, \u001b[39m0\u001b[39;49m, \u001b[39m1\u001b[39;49m, \u001b[39m0\u001b[39;49m, \u001b[39m1\u001b[39;49m, \u001b[39m0\u001b[39;49m, \u001b[39m0\u001b[39;49m]])\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/ryans/Desktop/Laptop%20Price%20Predictor/model/.ipynb_checkpoints/model_building.ipynb#Y104sZmlsZQ%3D%3D?line=1'>2</a>\u001b[0m pred_value\n",
      "File \u001b[1;32mc:\\Users\\ryans\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\ensemble\\_forest.py:984\u001b[0m, in \u001b[0;36mForestRegressor.predict\u001b[1;34m(self, X)\u001b[0m\n\u001b[0;32m    982\u001b[0m check_is_fitted(\u001b[39mself\u001b[39m)\n\u001b[0;32m    983\u001b[0m \u001b[39m# Check data\u001b[39;00m\n\u001b[1;32m--> 984\u001b[0m X \u001b[39m=\u001b[39m \u001b[39mself\u001b[39;49m\u001b[39m.\u001b[39;49m_validate_X_predict(X)\n\u001b[0;32m    986\u001b[0m \u001b[39m# Assign chunk of trees to jobs\u001b[39;00m\n\u001b[0;32m    987\u001b[0m n_jobs, _, _ \u001b[39m=\u001b[39m _partition_estimators(\u001b[39mself\u001b[39m\u001b[39m.\u001b[39mn_estimators, \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mn_jobs)\n",
      "File \u001b[1;32mc:\\Users\\ryans\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\ensemble\\_forest.py:599\u001b[0m, in \u001b[0;36mBaseForest._validate_X_predict\u001b[1;34m(self, X)\u001b[0m\n\u001b[0;32m    596\u001b[0m \u001b[39m\u001b[39m\u001b[39m\"\"\"\u001b[39;00m\n\u001b[0;32m    597\u001b[0m \u001b[39mValidate X whenever one tries to predict, apply, predict_proba.\"\"\"\u001b[39;00m\n\u001b[0;32m    598\u001b[0m check_is_fitted(\u001b[39mself\u001b[39m)\n\u001b[1;32m--> 599\u001b[0m X \u001b[39m=\u001b[39m \u001b[39mself\u001b[39;49m\u001b[39m.\u001b[39;49m_validate_data(X, dtype\u001b[39m=\u001b[39;49mDTYPE, accept_sparse\u001b[39m=\u001b[39;49m\u001b[39m\"\u001b[39;49m\u001b[39mcsr\u001b[39;49m\u001b[39m\"\u001b[39;49m, reset\u001b[39m=\u001b[39;49m\u001b[39mFalse\u001b[39;49;00m)\n\u001b[0;32m    600\u001b[0m \u001b[39mif\u001b[39;00m issparse(X) \u001b[39mand\u001b[39;00m (X\u001b[39m.\u001b[39mindices\u001b[39m.\u001b[39mdtype \u001b[39m!=\u001b[39m np\u001b[39m.\u001b[39mintc \u001b[39mor\u001b[39;00m X\u001b[39m.\u001b[39mindptr\u001b[39m.\u001b[39mdtype \u001b[39m!=\u001b[39m np\u001b[39m.\u001b[39mintc):\n\u001b[0;32m    601\u001b[0m     \u001b[39mraise\u001b[39;00m \u001b[39mValueError\u001b[39;00m(\u001b[39m\"\u001b[39m\u001b[39mNo support for np.int64 index based sparse matrices\u001b[39m\u001b[39m\"\u001b[39m)\n",
      "File \u001b[1;32mc:\\Users\\ryans\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\base.py:626\u001b[0m, in \u001b[0;36mBaseEstimator._validate_data\u001b[1;34m(self, X, y, reset, validate_separately, cast_to_ndarray, **check_params)\u001b[0m\n\u001b[0;32m    623\u001b[0m     out \u001b[39m=\u001b[39m X, y\n\u001b[0;32m    625\u001b[0m \u001b[39mif\u001b[39;00m \u001b[39mnot\u001b[39;00m no_val_X \u001b[39mand\u001b[39;00m check_params\u001b[39m.\u001b[39mget(\u001b[39m\"\u001b[39m\u001b[39mensure_2d\u001b[39m\u001b[39m\"\u001b[39m, \u001b[39mTrue\u001b[39;00m):\n\u001b[1;32m--> 626\u001b[0m     \u001b[39mself\u001b[39;49m\u001b[39m.\u001b[39;49m_check_n_features(X, reset\u001b[39m=\u001b[39;49mreset)\n\u001b[0;32m    628\u001b[0m \u001b[39mreturn\u001b[39;00m out\n",
      "File \u001b[1;32mc:\\Users\\ryans\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\base.py:415\u001b[0m, in \u001b[0;36mBaseEstimator._check_n_features\u001b[1;34m(self, X, reset)\u001b[0m\n\u001b[0;32m    412\u001b[0m     \u001b[39mreturn\u001b[39;00m\n\u001b[0;32m    414\u001b[0m \u001b[39mif\u001b[39;00m n_features \u001b[39m!=\u001b[39m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mn_features_in_:\n\u001b[1;32m--> 415\u001b[0m     \u001b[39mraise\u001b[39;00m \u001b[39mValueError\u001b[39;00m(\n\u001b[0;32m    416\u001b[0m         \u001b[39mf\u001b[39m\u001b[39m\"\u001b[39m\u001b[39mX has \u001b[39m\u001b[39m{\u001b[39;00mn_features\u001b[39m}\u001b[39;00m\u001b[39m features, but \u001b[39m\u001b[39m{\u001b[39;00m\u001b[39mself\u001b[39m\u001b[39m.\u001b[39m\u001b[39m__class__\u001b[39m\u001b[39m.\u001b[39m\u001b[39m__name__\u001b[39m\u001b[39m}\u001b[39;00m\u001b[39m \u001b[39m\u001b[39m\"\u001b[39m\n\u001b[0;32m    417\u001b[0m         \u001b[39mf\u001b[39m\u001b[39m\"\u001b[39m\u001b[39mis expecting \u001b[39m\u001b[39m{\u001b[39;00m\u001b[39mself\u001b[39m\u001b[39m.\u001b[39mn_features_in_\u001b[39m}\u001b[39;00m\u001b[39m features as input.\u001b[39m\u001b[39m\"\u001b[39m\n\u001b[0;32m    418\u001b[0m     )\n",
      "\u001b[1;31mValueError\u001b[0m: X has 31 features, but RandomForestRegressor is expecting 41 features as input."
     ]
    }
   ],
   "source": [
    "pred_value = best_model.predict([[8, 1.3, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0]])\n",
    "pred_value"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
