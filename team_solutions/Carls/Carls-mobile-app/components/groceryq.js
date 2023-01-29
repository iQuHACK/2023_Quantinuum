import React, {useState} from 'react';

import { View, Text, StyleSheet, TouchableOpacity, Image, Pressable } from 'react-native';


const Groc2 = (props) => {
  const [task, setTask] = useState();
  const [taskItems, setTaskItems] = useState([]);




  const completeTask = (index) => {
    let itemsCopy = [...taskItems];
    itemsCopy.splice(index, 1);
    setTaskItems(itemsCopy)
  }
  return (
<View>
              <Text style={styles.itemText}>{props.text}</Text>
            </View>
  );
}

const styles = StyleSheet.create({
  item: {
    marginLeft: -4,
    width: '79%',
    backgroundColor: '#FFF',
    padding: 15,
    borderRadius: 10,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 20,
    shadowColor: '#171717',
    shadowOffset: {width: -1, height: 2},
    shadowOpacity: 0.2,
    shadowRadius: 3,
  },
  itemquantity:{
    backgroundColor: '#FFF',
    width:'80%',  
    flexDirection: 'column',
    alignContent:'Center'
    
  
  },
  itemLeft: {
    flexDirection: 'row',
    
    flexWrap: 'wrap'
 
  },
  alignLeft: {
    flexDirection: 'row',

    flexWrap: 'wrap',

  },
  square: {
    alignContent: 'left',
    width: 24,
    height: 24,
    backgroundColor: '#29974D',

    borderRadius: 5,
    
  },

  itemminus: {
    maxWidth: '80%',
    paddingLeft: 24,
    paddingRight: 12,
    alignContent: 'center',
  },

  itemammount: {
    maxWidth: '80%',
    paddingLeft: 12,
    paddingRight: 12,
    alignContent: 'center',
  },
  itemadd: {
    maxWidth: '80%',
    paddingLeft: 12,
    paddingRight: 24,
    alignContent: 'center',
  },
  itemText2: {
    maxWidth: '80%',
    color: 'grey',
    paddingRight: 10,
    marginTop: 3
  },
  itemText: {
    maxWidth: '100%',
    fontWeight: 'bold',
    paddingBottom: 2,

  },

  circular: {


  },
});

export default Groc2;