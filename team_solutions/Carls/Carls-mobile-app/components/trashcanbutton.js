import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Image } from 'react-native';

import Ionicons from '@expo/vector-icons/Ionicons';
import { Octicons } from '@expo/vector-icons';
import { Feather } from '@expo/vector-icons';

const TrashCanButton = (props) => {
    return (
    <View style={styles.circular}>
      
         <Octicons name="trash" size={24} color="grey" />
    </View>

);
}
const styles = StyleSheet.create({
    circular: {


    },
  });
  
  export default TrashCanButton;