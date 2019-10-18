import { Button, Container, Content, Form, Input, Item, List, ListItem, Tab, Tabs, Text } from 'native-base';
import Header from '../Header';
import PropTypes from 'prop-types';
import React from 'react';
import Spacer from '../Spacer'

class GroupListing extends React.Component {
  state = {
    goals : [],
    weight: '',
    food: '',
    pain: '',
    physicalActivity: '',
    comments: ''
  };
  render() {
    return (
      <Container>
        <Content padder>
          <Header 
            align="center"
            title="Goals and Activity"
          />
          <Tabs>
            <Tab heading="Goal" key={1} style={{ padding: 10}}>
              <List>
                {this.state.goals && 
                <div>
                  <ListItem>
                      <Text style={{ fontWeight: '300' }}>{goal[0]}</Text>
                  </ListItem>
                  <ListItem>
                      <Text style={{ fontWeight: '300' }}>{goal[1]}</Text>
                  </ListItem>
                  <ListItem>
                      <Text style={{ fontWeight: '300' }}>{goal[2]}</Text>
                  </ListItem>
                </div>
              }
              </List>
            </Tab>
            <Tab heading="Activity Record" key={2} align="center">
              <Form>
                <Item>
                  <Input placeholder="Weight" onChangeText={text => this.setState({ weight: text })}/>
                </Item>
                <Item>
                  <Input placeholder="What did you eat today?" onChangeText={text => this.setState({ food: text })}/>
                </Item>
                <Item>
                  <Input placeholder="Does it pain? If yes, specify." onChangeText={text => this.setState({ pain: text})}/>
                </Item>
                <Item>
                  <Input placeholder="Did you perform any physical activity?" onChangeText={text => this.setState({ physicalActivity: text})}/>
                </Item>
                <Item>
                  <Input placeholder="Additional comments" onChangeText={text => this.setState({ comments: text})}/>
                </Item>
                <Spacer size={20} />
                <Item align="center">
                  <Button primary onPress={() => {
                      this.setState({
                        goals: ['Loose 1kg this week', 'Exercise for three hours this week', 'Eat more greens']
                      })
                  }}>
                    <Text>
                      Submit
                    </Text></Button>
                </Item>
              </Form>
            </Tab>
          </Tabs>
        </Content>
      </Container>
    );
  }
};

GroupListing.propTypes = {
  groupsQuery: PropTypes.shape({
    loading: PropTypes.bool,
    error: PropTypes.shape(),
    groups: PropTypes.arrayOf(PropTypes.shape()),
  }),
};

export default GroupListing;
