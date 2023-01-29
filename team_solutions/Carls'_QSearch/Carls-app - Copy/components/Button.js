import React from 'react';
import {TouchableOpacity, Text} from 'react-native';
import COLORS from '../src/colors';
const Button = ({title, onPress = () => {}}) => {
  return (
    <TouchableOpacity
      onPress={onPress}
      activeOpacity={0.7}
      style={{
        height: 55,
        width: '85%',
        backgroundColor: '#1BAC4B',
        marginVertical: 70,
        justifyContent: 'center',
        alignItems: 'center',
        borderRadius: 15,
        shadowColor: '#171717',
        shadowOffset: {width: -2, height: 4},
        shadowOpacity: 0.2,
        shadowRadius: 3,
      }}>
      <Text style={{color: COLORS.white, fontWeight: 'bold', fontSize: 18}}>
        {title}
      </Text>
    </TouchableOpacity>
  );
};

export default Button;