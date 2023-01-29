import React, {useState} from 'react';

import { View, Text, StyleSheet, ScrollView, Image, Pressable } from 'react-native';
import App from '../components/grocery_quantity_counter';
import Ionicons from '@expo/vector-icons/Ionicons';
import { Octicons } from '@expo/vector-icons';
import { Feather } from '@expo/vector-icons';
import TrashCanButton from './trashcanbutton';

const Task = (props) => {
  const [task, setTask] = useState();
  const [taskItems, setTaskItems] = useState([]);
  console.log("goes here")
  console.log(props.kroger)



  const completeTask = (index) => {
    let itemsCopy = [...taskItems];
    itemsCopy.splice(index, 1);
    setTaskItems(itemsCopy)
  }
  return (
    <View style={styles.item}>

        <ScrollView style={styles.long} horizontal>
              <Text style={styles.itemText}>{props.text}</Text>
              <Text style={styles.itemText}> ${props.kroger}</Text>
        </ScrollView>
         
      {/* delete from basket */}

    </View>
  );
}

const styles = StyleSheet.create({
  long:{
    width: '55%',
  },
  item: {
    marginLeft: 4,
    width: '95%',
    height: 55,
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

export default Task;