import React, {useState} from 'react';
import { View, Text, StyleSheet, ScrollView, Pressable } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { useNavigation } from '@react-navigation/native';

const Privacy = () => {
  const navigation = useNavigation();
const onPressW = () => {
    navigation.navigate('api_register',{})
   };
  return (
            <View style={styles.flex}>
              <ScrollView>
                <Text style={styles.textTitle}>Privacy Policy</Text>
                <Text style={styles.text}>I. Introduction and Overview
 
 Thank you for using the CleverCart Services! We are committed to providing you the best online shopping and delivery experience possible. This Privacy Policy explains what information Maplebear Inc. d/b/a CleverCart (“CleverCart”, “we”, or “us”) collects, how that information is used, under what circumstances we share information, and the choices you can make about that information. 
 
 This Privacy Policy applies whether you access the CleverCart Services (as defined in our Terms of Service) through a browser, a mobile application, or any other method.
 
 "Personal Information" or "PI" is information about you that may be used to identify you (such as your name, phone number, or address). Personal Information may also include health or medical information that relates to (a) your past, present, or future physical or mental health or condition, (b) the provision of health care to you, or (c) your past, present, or future payment for the provision of health care (“Personal Health Information” or “PHI”).
  
 Additional Disclosures
  
 We may provide different or additional disclosures relating to the processing of Personal Information of individuals who are residents of certain countries, regions or states. Listed below are additional disclosures that may be applicable to you.
 
 If you are a California resident, please see the additional privacy disclosures below in Disclosure For California Residents.
 
 If you are a Nevada resident, please see the additional privacy disclosures below in Disclosure For Nevada Residents.
 
 If you are a resident of Canada, please see the additional privacy disclosures in Disclosure For Canada Residents.
  
 II. Information We Collect
  
 A. Information You Provide to Us or Allow Others to Provide to Us
 
  Account Creation and Orders
 At various points in the CleverCart experience, you may provide us with information about yourself. For example, when you create an account through the Services, you provide us with personal information like your name, email address, and zip or postal code. You may also provide us with information about your taste preferences and who you shop for. And if you place an order through the Services, we collect information including your physical address, phone number, birth date, driver’s license expiration date (for alcohol orders, prescription deliveries, or orders that are age-restricted or exceed a certain dollar amount, where available), credit card information, vehicle license plate number(s) (for curbside pickup orders) and the details of your order.
 
 If you use the Services for prescription delivery (where available), the third-party pharmacy processing your prescription will provide us with your name, address, email address, birth date, phone number, the total amount being charged to you for the prescription drug product(s), and sales tax information for the prescription drug product(s) (if applicable). The third-party pharmacy will also share whether or not the prescription drug product you have ordered requires temperature control. If a prescription drug product delivered to you through the Services has been recalled, the third-party pharmacy will share your name, email address, the date of the prescription drug product order, and the total amount to be refunded to you with CleverCart. The pharmacy will not disclose to us the name, quantity, manufacturer or distributor of the prescription drug you have ordered, or any other PHI about you, other than your status as a patient of the pharmacy.
 
 We may also collect health information that you provide directly to us regarding an experience with a retail partner, which may require us to contact that retailer, or other retailer partners, for public health or safety reasons, or to facilitate a refund. We do not share your identity with the retailers we contact in such capacity, but may share the date, time and location of a transaction, which may allow a retailer to independently identify you.
 
 If you log into the Services through a third-party service, both we and that third-party may receive some information about you and your use of the Services. For example, if you choose to log into the Services with your Facebook or Google account, we may receive information from these companies, such as your name, e-mail address, public profile information, and information about your contacts. We may also offer social sharing tools (such as a “Like” button) that let you share actions on the Services with other websites and vice versa. In those cases, the providers of those tools may receive information about you when you use those tools. You should check the privacy policies of these third-party services and your settings there for more information.
 
 Our partners may let us collect information about use of their sites/apps or share such information with us. For example, if you use an CleverCart button or widget on another site or app, we may receive information about your use of that button or widget and the third-party site/app. We also may collect information about you from partners with whom we work for advertising measurement, attribution and analytics; from partners who assist us in payment collection, preventing or addressing fraud, or to assist us in connection with claims or disputes; from publicly-available sources; and from law enforcement, public health and other governmental authorities.
 
 If you wish to invite your friends and contacts to use the Services, we will give you the option of either manually submitting their contact information or, for United States residents, importing it from your address books on other third-party services. In both cases, we will store this information for the sole purposes of allowing you to send your friends referral offers, for determining whether your friends use the Services after a referral is sent, and, for United States residents, to remind your friends of the referral sent on your behalf.
  
 Community Affairs
 CleverCart is active in local communities as part of our mission to create a world where everyone has access to the food they love and more time to enjoy it together. You may provide us your information in connection with our community affairs efforts.
  
 Location Information
 When you use the Services, we may collect location data. For instance, if you allow the Services to access location services through the permission system used by your device's mobile operating system or browser, we may collect the precise location of your device. We use your location information to facilitate the prompt hand-off of pickup orders (where available), to assist you in finding nearby stores for which pickup or delivery are available, for other similar purposes and for analytics purposes. You can choose whether or not to enable the location tracking feature through the settings on your device or browser, or when prompted by the CleverCart mobile app. We may also infer your general location information, for example by using your internet protocol (IP) address.
 
 B. Technical Information about Usage of the Services
  
 When you use the Services, or browse our sites, either through a browser or mobile app, we automatically receive some technical information - device and usage information - about the hardware and software that are being used.
 
 Cookies, Pixels, and Other Tracking Technologies
 We, our partners, advertisers, and third-party advertising networks use various technologies to collect information, including but not limited to cookies, pixels, scripts, SDKs and device identifiers. Cookies are small text files that are sent by your computer when you access our services through a browser. We, our partners, advertisers, and third-party advertising networks may use session cookies (which expire when you close your browser), persistent cookies (which only expire when you choose to clear them from your browser), pixels, scripts, and other identifiers to collect information from your browser or device that helps us do things such as understand how you use our Services and other services; personalize your experience; measure, manage, and display advertising on the Services or on other services; understand your usage of the Services and other services in order to serve customized ads; and remember that you are logged into the Services. Our partners, advertisers, and third-party advertising networks may use these technologies to collect information about your online activity over time and across different websites or online services. By using your browser settings, you may block cookies or adjust settings for notifications when a cookie is set. 
 
  We work with third-party companies to help us understand the usage of the Services and the performance of advertising, and these third parties may also deploy cookies, pixels, or other identifiers on the Services or collect information through our mobile applications. For example, we use Google Analytics to understand how users interact with various portions of the Services -- you can learn more about information that Google may collect here.
 
  Log Information
 When you use the Services, or browse our sites, our servers will record information about your usage of the Services and information that is sent by your browser or device. Log information can include things like the IP address of your device, information about the browser, operating system and/or app you are using, unique device identifiers, pages that you navigate to and links that you click, searches that you run on the Services, and other ways you interact with the Services. If you are logged into the Services, this information is stored with your account information.
 
  Interest-Based or Online Behavioral Advertising
 CleverCart may use third-party advertising companies to serve interest-based advertisements to you. These companies compile information from various online sources (including mobile-enabled browsers and applications) to match you with ads that will be the most relevant, interesting, and timely for you. If you would like to opt-out of interest-based advertising, please visit http://optout.networkadvertising.org/#/. Please note that you will be opted out of all interest-based advertising from all business members of the Network Advertising Initiative for that specific browser on that specific device. If you opt-out, you may continue to see CleverCart’s or our partners’ online advertisements; however, these ads will not be as relevant to you.
 
  Do Not Track
 Your browser settings may allow you to automatically transmit a "Do Not Track" signal to online services you visit. CleverCart does not respond to "Do Not Track" signals. For more information, visit www.allaboutdnt.com.
 
 C. Children
  
 
 Our Services are not intended for children under 18 years of age, and we do not knowingly collect Personal Information (as defined by the U.S. Children’s Online Privacy Protection Act, or “COPPA”) in a manner not permitted by COPPA. If we obtain actual knowledge that any information we collect has been provided by a child under the age of 18, we will delete that information to the extent required by applicable laws.
 
 We do not knowingly “sell,” as that term is defined under the California Consumer Protect Act (“CCPA”), the Personal Information of minors under 18 years old who are California residents.
 
 III. How We Use Your Information
  
 We use the information we collect for various purposes, including to:
 
  
 
 Provide and improve the quality of the Services, and develop new products and services
 
 Allow your personal shopper (meaning those that shop for and/or deliver the order for you, including our retail partners and their employees/agents where applicable or our third-party providers) to choose your items at retailer sites, deliver your items to you, and/or call or text you with any updates or issues
 
 Charge you for the purchase and delivery costs through one or more payment processing partners
 
 Offer you customized content (including advertising, coupons, and promotions)
 
 Understand how users interact with the Services (including advertising both on and off the Services) as a whole and to test new features or changes in our features
 
 Provide customer service, respond to your communications and requests, and contact you about your use of the Services
 
 Send you messages related to our community affairs efforts
 
 Fulfill any other business or commercial purposes at your direction or with prior notice to you and your consent
 
 You can opt-out of receiving promotional communications from CleverCart by using the settings on the Account Info page or by using the unsubscribe mechanism included in the message, where applicable.
 
 IV. What We Share
  
 The Services comprise a platform that presents you with a set of one or more retailer virtual storefronts from which you can select goods for picking, packing, and delivery by individual Personal Shopper(s) to your location or, if available, for you to pick up in-store. In order to make this work, we need to share information about you and your order with the other parties who help enable the service. This includes, for example, the Personal Shopper(s) who pick and deliver your order, the payment processing partner(s) that we use to validate and charge your credit card, and the retail partner(s) from which you are purchasing goods. To be clear, only our payment processing partner(s) receive credit card information.
 
 We also share information under the following principles:
 
 With your consent or at your direction— We will share your information with entities outside of the Services when we have your consent to do so or it is done at your direction. For example:
 
 If you enter loyalty card information from a particular retailer, we share that information with the retailer you chose along with your order so that information can be added to your loyalty card account.
 
 If you share a recipe publicly on the Services, it is viewable by anyone along with your first name and last initial.
 
 If you invite friends to use the Services through our referral program or to share a shopping cart, we will share some information with the friends you invite like your name and picture. Likewise, if you choose to join someone else’s cart, they will see some of your information.
 
 With our retail partners — We may share your information with our retail partners in order to provide and maintain the Services.
 
 For external processing or service provision — We sometimes share information with third parties to process information on our behalf or to otherwise provide certain services (such as delivery services, advertising services, or information to better tailor our services to you). For the purposes of this processing or provision of services, we may share your information with such third parties under appropriate confidentiality provisions.
 
 For legal purposes — We may share your information when we believe that the disclosure is reasonably necessary to (a) comply with applicable laws, regulations, legal process, or requests from law enforcement or regulatory authorities, (b) prevent, detect, or otherwise handle fraud, security, or technical issues, and (c) protect the safety, rights, or property of any person, the public, or CleverCart.
 
 On a non-personal or aggregate basis — We share information on both a non-personally identifying basis (including, but not limited to, order and delivery details but not including credit card information) or an aggregate basis.
 
 To enable purchase of alcohol (not available in all jurisdictions) — When you buy alcohol using the Services, we may be required by law to share certain information with the retailer who makes the sale. This information could include, among other things, the names and addresses of the purchaser and recipient, government issued ID information, the quantity, brand, price, proof, and volume of alcohol purchased, and a recipient signature.
 
 For business purposes - We may share you information in connection with, or during negotiations of any merger, sale of company assets, financing, restructuring (including transfers made as a part of insolvency or bankruptcy proceedings) or acquisition of all or a portion of our business by another company. We may also share your information between and among CleverCart, and its current and future parents, affiliates, subsidiaries, and other companies under common control and ownership.
  
 
 V. Personal Health Information
  
 
 This Section (Personal Health Information) governs our use and disclosure of your Personal Health Information. If there is a conflict between the terms of this Section and any other terms of this Privacy Policy or the CleverCart Terms of Services, the terms in this Section will govern. To the extent we receive, create, maintain, use or disclose any of your PHI, we will maintain the privacy and security of such information as required by the federal patient privacy law known as the Health Insurance Portability and Accountability Act and the regulations promulgated under that Act ("HIPAA"), as well as any applicable state and other federal privacy policy laws.
 
 Your PHI is protected under HIPAA and under certain state laws. Those laws give you rights with respect to the access, use, and disclosure of PHI by your health care providers, such as pharmacies, and us. When you place a pharmacy order using our Services, the pharmacy responds as we have described above under the Section entitled "Information we collect" by disclosing to CleverCart your status as a patient of the pharmacy. Information concerning your status as a patient of the pharmacy is PHI and protected by HIPAA. As discussed above, no other PHI will be disclosed to us by your pharmacy and no other PHI will be disclosed by CleverCart to your personal shopper other than your status as a patient of the pharmacy. For a more complete description of your rights under HIPAA and the uses and disclosures of your PHI, please refer to your pharmacy's Notice of Privacy Practices. We will not disclose your PHI without your prior written consent with other people or non-affiliated companies unless: (i) it is needed to provide our Services, (ii) it has been "de-identified" so that it cannot identify you, (ii) we have your prior written consent, (iv) disclosure is required by law, or (v) we are acquired or file for bankruptcy.
 
 VI. Security
  
 We employ and maintain reasonable administrative, physical, and technical measures designed to safeguard and protect information under our control from unauthorized access, use, and disclosure. In addition, when we collect, maintain, access, use, or disclose your PHI, we will do so using systems and processes consistent with information privacy and security requirements under applicable federal and state laws, including, without limitation, HIPAA. All electronic PHI will be encrypted at rest and in transit. Nevertheless, transmission via the internet is not completely secure and we cannot guarantee the security of information about you.
 
  
 
 We will make any legally required notifications of any breach of the security, confidentiality, or integrity of your PHI or PI, including, without limitation, breaches of your stored PHI or PI (as breaches are defined under applicable state or federal statutes on security breach notification). To the extent permitted by applicable laws, we will make such notifications to you without unreasonable delay, as consistent with (i) the legitimate needs of law enforcement or (ii) any measures necessary to determine the scope of the breach and restore the reasonable integrity of the data system.
 
 VII. Your Choices
 
 We provide you with the right to access or request the deletion of your Personal Information. You may also correct or update your account information.
 
 Correcting or Updating your Account Information
 You may update your name, telephone number, address and payment information by logging into your CleverCart account and visiting the “Account Settings” page. You may also view existing and past orders. 
 
 Requesting Access to or Deletion of your Personal Information
 You may request access to the Personal Information we collected in the past twelve (12) months and you may request the deletion of your Personal Information. Note that access and deletion requests are subject to certain exceptions, including to protect the security of the information and of your account.
 
 Account Holders. If you are an CleverCart account holder, click here to exercise these choices. For verification purposes, you will be prompted to re-log into the Services.
 
 Non-Account Holders. If you do not have an CleverCart account or are unable to log into the Services, you may contact us at customerprivacy@CleverCart.app.
 
 Authorized Agents. If you have designated an authorized agent to submit requests on your behalf, the authorized agent must submit requests at customerprivacy@CleverCart.app. Before processing a request from an authorized agent, we require written proof of the authorization you have provided the agent and will also verify your identity directly.
  
 
 VIII. Changes to this Policy
 CleverCart may occasionally update this Privacy Policy. If we make changes, we will notify you by revising the date at the top of this Privacy Policy and, in the case of material changes to the Privacy Policy, we may provide you with additional notice (such as a notice in our user interface or sending you a notification by email). Use of the CleverCart Services following an update to this Privacy Policy constitutes consent to the updated Privacy Policy.
 
  
 
 IX. Disclosures for Residents of California
  
 Only to individuals who reside in California. The California Consumer Privacy Act of 2018 (“CCPA”) provides California residents certain additional notice rights. 
 
  
 
 A. Notice of Collection
  
 Although the information we collect is described in greater detail in  Section II above, the categories of Personal Information that we have collected – as described by the CCPA – including in the past 12 months are:
 
 Identifiers - including name, email address, and IP address.
 
 Other individual customer records - including phone number , billing and shipping address, and credit or debit card information. This category includes Personal Information protected under pre-existing California law (Cal. Civ. Code 1798.80(e)), and overlaps with other categories listed here
 
 Demographics - including your age. This category includes data that may qualify as protected classifications under other California or federal laws.
 
 Commercial information - including purchases and engagement with our Services.
 
 Internet activity - including your interactions with our Service.
 
 Geolocation data - including location enabled services such as WiFi and GPS.
 
 Sensory Information - such as recordings of phone calls between you and us and surveillance video at our properties, where permitted by law.
 
 Inferences - including information about your interests, preferences and favorites.
 
 Health Information - including any information you provide to us regarding an experience with a retailer that may require us to contact that retailer or other retailer partners for public health or safety reasons, or to facilitate a refund. We do not share your identity with retailers we may contact in such a capacity, but do share date, time and location of a transaction, which may allow a retailer to independently identify you.
 
 For more information on our collection practices, including the sources we receive information from, please review “ Information We Collect” (Section II above). We collect and use these categories of Personal Information for the business purposes described in “ How We Use Your Information” (Section III above), including to provide and manage our Services.
 
  
 
 We disclose the following categories of Personal Information to third parties for our commercial purposes: identifiers, demographic information, commercial information, relevant order information, internet activity, geolocation data, sensory information, and inferences. We partner with different types of entities to assist with our daily operations and manage our Services. Please review “ What We Share” (Section IV above) for more detail about the third parties we have shared information with and the underlying principles that guide our sharing practices.
 
 B. Right to Know and Delete
 
 California residents have the right to delete the personal information we have collected from you, and the right to know certain information about our data practices in the preceding twelve (12) months. In particular, you have the right to request the following from us:
 
 The categories of personal information we have collected about you;
 
 The categories of sources from which the personal information was collected;
 
 The categories of personal information about you we disclosed for a business purpose or sold;
 
 The categories of third parties to whom the personal information was disclosed for a business purpose or sold;
 
 The business or commercial purpose for collecting or selling the personal information; and
 
 The specific pieces of personal information we have collected about you.
 
 To request access to or deletion of your information, please see Section VII ( Your Choices) above.
 
  
 C. Right to Opt-Out
 We do not generally sell information as the term “sell” is traditionally understood. However, if and to the extent “sale” under the CCPA is interpreted to include advertising technology activities such as those implemented specifically for interest-based advertising, we will comply with applicable law as to such activity.
 
 D. Right to Non-Discrimination
 You have the right not to receive discriminatory treatment by us for the exercise of any your rights.
 
 E. Financial Incentives
 Financial incentives are programs, benefits, or other offerings, including payments to consumers as compensation, for the disclosure, deletion, or sale of personal information about them. We offer a number of promotions and other incentives at any given time, each with their own individual terms. For a list and more details about our current promotions and other incentives, please visit our “Terms of Promos and Credits” page which lists each promotion and links its respective terms here. Your intentional participation in any of the programs, benefits, or other offerings under this Section will be interpreted as affirmative consent to the terms of such incentive.
 
 For example, we offer a referral rewards program to our users who recommend our services to their contacts as prospective customers, when those prospective customers sign up for, and make a purchase using our Services. We generally do not treat consumers differently if they exercise a right under California law. However, in certain circumstances, discounted prices or rewards will require you to be part of the particular program. In such circumstances, we may offer a price difference because the price is reasonably related to the value of your data.
 
 F. Shine the Light
 If you are a California resident, you may ask CleverCart for a notice describing what categories of personal information CleverCart shares with third parties or affiliates for those third parties or affiliates’ direct marketing purposes and identify the name and address of the third parties that received such personal information. Please submit a written request to the address provided below and specify you want a copy of your California Shine the Light Notice. We may require additional information from you to allow us to verify your identity and are only required to respond to requests once during any calendar year.
 
 G. Consumer Affairs
 
 Under California Civil Code Section 1789.3, California residents are entitled to the following specific consumer rights notice: If you have a question or complaint regarding our website, please send an email to legal@clevercart.app. You may also contact us by writing to us at the address provided below under the Section entitled “Contact Information”. California residents may reach the Complaint Assistance Unit of the Division of Consumer Services of the California Department of Consumer Affairs may be contacted in writing at 400 R Street, Suite 1080, Sacramento, California 95814, or by telephone at (916) 445-1254 or (800) 952-5210.
 
  
 
 X. Disclosure for Residents of Nevada
  
 
 We do not sell Personal Information as defined under Nevada law.
 
  
 
 XI. Disclosure for Residents of Canada
  
 
 CleverCart is located in the United States and some of its service providers (including affiliates acting in this capacity) are located in the United States or elsewhere outside of Canada. As a result, your Personal Information will be processed and stored outside of Canada for the purposes described in this Privacy Policy. While outside of Canada, Personal Information will be subject to applicable local laws, which may permit government and national security authorities in those jurisdictions to access your Personal Information in certain circumstances.
 
 The file containing your Personal Information will be maintained on our servers (or those of our service providers) and will be accessible by our authorized employees, representatives and service providers who require access for the purposes described in this Privacy Policy. You may request access to or correction of your Personal Information, or withdraw consent to our collection, use or disclosure of your Personal Information, as explained in Section VII (Your Choices) above. These rights are subject to applicable contractual and legal restrictions and reasonable notice. We may take reasonable steps to verify your identity before honoring any such requests.
 </Text>
 <Pressable onPress={onPressW}>
          <LinearGradient
        colors={['#1BAC4B', '#46D375']}
        style={styles.logoutbutton}>
        <Text style={styles.logouttext}>Yes I have Read it</Text>
      </LinearGradient>
                </Pressable >
              </ScrollView>
            </View>
  );
}

const styles = StyleSheet.create({
textTitle: {
    maxWidth: '100%',
    fontWeight: 'bold',
    fontSize: 24,
    textAlign: 'center'
  },
  text: {
    maxWidth: '100%',
    fontSize: 12,
  },
  flex: {
    flex:1,
    alignSelf: 'center',
    width:'95%',
    height: '100%',
    paddingTop: 30
  },
  logoutbutton: {
    width: 300,
    height: 60,
    marginVertical:12,
    justifyContent: 'center',
    borderRadius:30,
    shadowColor: '#171717',
    shadowOffset: {width: -2, height: 4},
    shadowOpacity: 0.2,
    shadowRadius: 3,
    marginTop: 15,
    alignSelf: 'center'
  },
  logouttext: {
    textAlign: 'center',
    color:'#fff',
    fontSize: 15,
  },
});


export default Privacy;