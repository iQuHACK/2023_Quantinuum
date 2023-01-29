import React, {useEffect, useState} from 'react';
import { KeyboardAvoidingView, Image, StyleSheet, Text, View, TextInput, TouchableOpacity, Keyboard, ScrollView } from 'react-native';
import FreeTrialEnd from './src/screens/settings/freetrialend';
import IndexTest from './src/nav/indextest';
import Navigation from './src/nav/nav1';
import {Amplify, API, graphqlOperation, Auth} from 'aws-amplify';
import awsconfig from './src/aws-exports';
import {withAuthenticator, AmplifyTheme} from 'aws-amplify-react-native';
import { NavigationContainer,DrawerActions } from '@react-navigation/native';
import {getUser} from './src/graphql/queries';
import {createUser} from './src/graphql/mutations';



Amplify.configure(awsconfig);

const App1 = () => {



 
  return(
    <NavigationContainer>
       <Navigation/>
    </NavigationContainer>
    
  );
};
const signUpConfig = {
  header: "Create your CleverCart account",

  hideAllDefaults: true,
  

  signUpFields: [
    {
      label: "Address(Street Address, City, State and ZIP)",
      key: "address",
      required: true,
      displayOrder: 2,
      type: "address",
    },
    {
      label: "Email",
      key: "email",
      required: true,
      displayOrder: 1,
      type: "string",
    },
    {
      label: "Username",
      key: "preferred_username",
      required: true,
      displayOrder: 3,
      type: "string",
    },
    {
      label: "Password",
      key: "password",
      required: true,
      displayOrder: 4,
      type: "password",
    },
  ],
};



const customTheme = {...AmplifyTheme,
  
  button:
  {...AmplifyTheme.button,
    backgroundColor: '#1BAC4B',
    borderRadius: 15},
  	buttonDisabled: {...AmplifyTheme.buttonDisabled,
      backgroundColor: '#E5E5E5',
      borderRadius: 15
    },
    sectionFooterLink: {
      ...AmplifyTheme.sectionFooterLink,
      color: '#61C99C',
      alignItems: 'baseline',
      textAlign: 'center',
    },
    sectionHeader:{
      ...AmplifyTheme.sectionheader,
      paddingBottom: 15    },
    input: {
      ...AmplifyTheme.input,
      borderRadius:15,
      marginBottom: -10
      
    },
  };



export default App1;