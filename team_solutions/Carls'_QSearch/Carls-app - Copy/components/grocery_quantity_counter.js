import React, { Component } from "react";
import { StyleSheet, Text, TouchableOpacity, View } from "react-native";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = { count:1 };
  }

  onPress = () => {
    this.setState({
      count: Math.min((this.state.count + 1),99)
    });
  };
    onPress2 = () => {
    this.setState({
      count: Math.max((this.state.count - 1),1)
    });
  };

  render() {
    const { count } = this.state;
    return (

      <View style={styles.container2}>
         <TouchableOpacity
          
          onPress={this.onPress2}
        >
         <View style={styles.minus}>
        
          <Text  style={styles.minustext}>-</Text>
        
         </View>
         </TouchableOpacity>

        <View style={styles.countContainer}>
          <Text style={styles.grey}>{count}</Text>
        </View>
        <TouchableOpacity onPress={this.onPress}>
        <View style={styles.plus}>
          <Text style={styles.plustext}>+</Text>
          </View>
        </TouchableOpacity>
          
      </View>
    );
  }
}

const styles = StyleSheet.create({
 container2:{
    flexDirection: 'row',
    alignItems: 'center',
    flexWrap: 'wrap',

 },
  minustext:{
    flexDirection: 'row',
    alignItems: 'center',
    flexWrap: 'wrap',
    paddingLeft: 6,
    paddingRight: 4,
    
    color: 'grey',
    
    fontWeight: 'bold',
    fontSize: 16
 },
 minus:{
  marginVertical: 1,
  marginHorizontal: 6,
  borderRadius: 10,
  backgroundColor: 'white',

 },
 plus:{
  borderRadius: 10,
  marginHorizontal: 6

 },
 plustext:{
  flexDirection: 'row',
  alignItems: 'center',
  flexWrap: 'wrap',
  paddingLeft: 4,
  paddingRight: 6,
  color: 'grey',
  fontWeight: 'bold',
  fontSize: 16

},
 grey:{
  color: 'grey',

 },

});

export default App;