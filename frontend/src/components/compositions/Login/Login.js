import React, { Component } from 'react';
import { withTranslation } from 'react-i18next';
import {
  EuiFieldPassword,
  EuiFieldText,
  EuiForm,
  EuiFormRow,
  EuiText,
  EuiSpacer,
  EuiButton,
  EuiFlexGroup,
  EuiFlexItem,
  EuiLink,
} from '@elastic/eui';
import { saveUserData } from '../../../utils';
import LoginUserMutation from './LoginUserMutation';
import { withRouter } from 'found';
import { AppContext } from '../../../contexts/AppContext';
class Login extends Component {
  state = {
    email: '',
    password: '',
    showErrors: false,
  };
  constructor(props) {
    super(props);
  }

  render() {
    const { t } = this.props;
    const errors = [t('errors.invalid-login')];

    return (
      <div>
        <EuiText grow={false}>
          <h2>{t('login-title')}</h2>
        </EuiText>

        <EuiForm>
          <form
            onSubmit={e => {
              e.preventDefault();
              this._login();
            }}
          >
            <span>
              <EuiFormRow
                label={t('login.email')}
                isInvalid={this.state.showErrors}
                error={errors}
              >
                <EuiFieldText
                  name="email"
                  icon="user"
                  placeholder={t('login.enter-email')}
                  value={this.state.email}
                  onChange={e => {
                    this.setState({ email: e.target.value });
                    this._toggleError(false);
                  }}
                  isInvalid={this.state.showErrors}
                />
              </EuiFormRow>
              <EuiFormRow
                label={t('login.password')}
                isInvalid={this.state.showErrors}
              >
                <EuiFieldPassword
                  placeholder={t('login.enter-password')}
                  name="password"
                  value={this.state.password}
                  onChange={e => {
                    this.setState({ password: e.target.value });
                    this._toggleError(false);
                  }}
                  isInvalid={this.state.showErrors}
                />
              </EuiFormRow>
              <EuiSpacer />
              <EuiFlexGroup
                justifyContent="spaceBetween"
                gutterSize="xl"
              >
                <EuiFlexItem>
                  <EuiButton type="submit" fill>
                    {t('login.login')}
                  </EuiButton>
                </EuiFlexItem>
                <EuiFlexItem className="pt3">
                  <EuiText size="m">
                    <EuiLink href="#">
                      {t('login.forgot-password')}
                    </EuiLink>
                  </EuiText>
                </EuiFlexItem>
              </EuiFlexGroup>
            </span>
          </form>
        </EuiForm>
      </div>
    );
  }
  _toggleError = isShow => {
    this.setState({
      showErrors: isShow,
    });
  };
  _login = () => {
    const { email, password } = this.state;

    LoginUserMutation(email, password, (response, errMessage) => {
      if (errMessage == null) {
        const { user, token, refreshToken } = response.login;

        saveUserData(JSON.stringify(user), token, refreshToken);

        this._toggleError(false);
        window.location.reload(true);
      } else {
        this._toggleError(true);
      }
    });
  };
}
Login.contextType = AppContext;
export default withTranslation()(withRouter(Login));
