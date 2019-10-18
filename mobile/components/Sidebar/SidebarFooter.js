import * as WebBrowser from 'expo-web-browser';
import { Icon } from "native-base";
import { Linking, Text, TouchableOpacity, View } from "react-native";
import React from "react";
import theme from "../../native-base-theme/variables/commonColor";

const styles = {
  footer: {
    flexDirection: "column",
    justifyContent: "space-evenly",
    padding: 5,
    marginBottom: 13
  },
  iconContainer: {
    color: theme.brandPrimary
  },
  footerText: {
    fontSize: 10,
    color: "grey"
  },
  socialContainer: {
    flexDirection: "row",
    justifyContent: "space-evenly",
    padding: 5
  },
  footerTextContainer: {
    flexDirection: "row",
    justifyContent: "space-evenly",
    color: "grey",
    padding: 5,
    paddingTop: 10
  }
};

const openLink = link => Linking.openURL(link).catch(err => console.log(err));

const SidebarFooter = () => (
  <View style={styles.footer}>
    <View style={styles.socialContainer}>
      <TouchableOpacity onPress={() => openLink("tel://+85234619827")}>
        <Icon style={styles.iconContainer} type="FontAwesome" name="phone" />
      </TouchableOpacity>
      <TouchableOpacity onPress={() => openLink("mailto:hia@hia.org.hk")}>
        <Icon style={styles.iconContainer} type="MaterialIcons" name="email" />
      </TouchableOpacity>
    </View>
    <TouchableOpacity
      style={styles.footerTextContainer}
      onPress={() => openLink("mailto:hia@hia.org.hk")}
    >
      <Text style={styles.footerText}>Developed by Team 2</Text>
    </TouchableOpacity>
    <TouchableOpacity
      style={styles.footerTextContainer}
      onPress={() =>
        WebBrowser.openBrowserAsync(
          "https://www.freeprivacypolicy.com/blog/privacy-policy-url/"
        )
      }
    >
      <Text style={{ ...styles.footerText, textDecorationLine: "underline" }}>
        Privacy Policy
      </Text>
    </TouchableOpacity>
  </View>
);

export default SidebarFooter;
