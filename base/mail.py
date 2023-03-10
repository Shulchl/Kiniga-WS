from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import ssl
import os
import json

from base.struct import Config


class Mail():

    def __init__(self, email, mailhtml, mailtxt) -> None:
        
        with open('config.json', 'r') as f:
            self.cfg = Config(json.loads(f.read()))

        self.smtp_server = self.cfg.bot_mailhost
        self.port = 587  # For starttls
        self.sender_email = self.cfg.bot_mail
        self.password = self.cfg.bot_mailpass

        self.email = email
        self.mailhtml = mailhtml
        self.mailtxt = mailtxt

    async def sendMail(self) -> None:

        receiver_email = self.email

        # Create the plain-text and HTML version of your message
        html = self.mailhtml

        message = MIMEMultipart("alternative")
        message["Subject"] = "E-mail de Resposta!"
        message["From"] = self.sender_email
        message["To"] = receiver_email #','.join(receiver_email)

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(MIMEText(html, "html"))

        # add images
        # files = ['image-1.png',
        #         'image-2.png',
        #         'image-3.png',
        #         'image-4.png',
        #         'image-5.png',
        #         'image-6.png']
        # Get the files/images you want to add.
        img_dir = "src\imgs\other\mail"
        images = [os.path.join(img_dir, i) for i in os.listdir(img_dir)]

        # Added a enumerate loop around the whole procedure.
        # Reference to cid:image_id_"j", which you will attach to the email later.
        for j, val in enumerate(images):

            with open('{}'.format(val), "rb") as attachment:
                msgImage = MIMEImage(attachment.read(), filename='filename')

            # print(j, val, '<image{}>'.format(j+1))
            # Define the image's ID with counter as you will reference it.
            msgImage.add_header('Content-ID', '<image%s>' % (j+1, ))
            message.attach(msgImage)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            # server.set_debuglevel(1)
            server.ehlo()
            server.login(self.sender_email, self.password)
            server.sendmail(
                self.sender_email, receiver_email, message.as_string()
            )

    def getEmailMessage(status):
        if status == 'accept':
            email = """\
                <!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
                <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
                <head>
                <!--[if gte mso 9]>
                <xml>
                <o:OfficeDocumentSettings>
                    <o:AllowPNG/>
                    <o:PixelsPerInch>96</o:PixelsPerInch>
                </o:OfficeDocumentSettings>
                </xml>
                <![endif]-->
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta name="x-apple-disable-message-reformatting">
                <!--[if !mso]><!--><meta http-equiv="X-UA-Compatible" content="IE=edge"><!--<![endif]-->
                <title></title>
                
                    <style type="text/css">
                    @media only screen and (min-width: 620px) {
                .u-row {
                    width: 600px !important;
                }
                .u-row .u-col {
                    vertical-align: top;
                }

                .u-row .u-col-100 {
                    width: 600px !important;
                }

                }

                @media (max-width: 620px) {
                .u-row-container {
                    max-width: 100% !important;
                    padding-left: 0px !important;
                    padding-right: 0px !important;
                }
                .u-row .u-col {
                    min-width: 320px !important;
                    max-width: 100% !important;
                    display: block !important;
                }
                .u-row {
                    width: calc(100% - 40px) !important;
                }
                .u-col {
                    width: 100% !important;
                }
                .u-col > div {
                    margin: 0 auto;
                }
                }
                body {
                margin: 0;
                padding: 0;
                }

                table,
                tr,
                td {
                vertical-align: top;
                border-collapse: collapse;
                }

                p {
                margin: 0;
                }

                .ie-container table,
                .mso-container table {
                table-layout: fixed;
                }

                * {
                line-height: inherit;
                }

                a[x-apple-data-detectors='true'] {
                color: inherit !important;
                text-decoration: none !important;
                }

                table, td { color: #000000; } #u_body a { color: #0000ee; text-decoration: underline; } @media (max-width: 480px) { #u_content_image_1 .v-src-width { width: auto !important; } #u_content_image_1 .v-src-max-width { max-width: 38% !important; } #u_content_image_2 .v-src-width { width: auto !important; } #u_content_image_2 .v-src-max-width { max-width: 100% !important; } }
                    </style>
                
                

                <!--[if !mso]><!--><link href="https://fonts.googleapis.com/css?family=Lato:400,700&display=swap" rel="stylesheet" type="text/css"><link href="https://fonts.googleapis.com/css?family=Montserrat:400,700&display=swap" rel="stylesheet" type="text/css"><!--<![endif]-->

                </head>

                <body class="clean-body u_body" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #ecf0f1;color: #000000">
                <!--[if IE]><div class="ie-container"><![endif]-->
                <!--[if mso]><div class="mso-container"><![endif]-->
                <table id="u_body" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #ecf0f1;width:100%" cellpadding="0" cellspacing="0">
                <tbody>
                <tr style="vertical-align: top">
                    <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                    <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #ecf0f1;"><![endif]-->
                    

                <div class="u-row-container" style="padding: 0px;background-color: transparent">
                <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #264653;">
                    <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                    <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #264653;"><![endif]-->
                    
                <!--[if (mso)|(IE)]><td align="center" width="600" style="width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
                <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                <div style="height: 100%;width: 100% !important;">
                <!--[if (!mso)&(!IE)]><!--><div style="height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
                
                <table id="u_content_image_1" style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                    <tr>
                    <td style="overflow-wrap:break-word;word-break:break-word;padding:20px 10px;font-family:'Montserrat',sans-serif;" align="left">
                        
                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                    <td style="padding-right: 0px;padding-left: 0px;" align="center">
                    <a href="https://kiniga.com/" target="_blank">
                    <img align="center" border="0" src="cid:image3" alt="Logo" title="Logo" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 21%;max-width: 121.8px;" width="121.8" class="v-src-width v-src-max-width"/>
                    </a>
                    </td>
                </tr>
                </table>

                    </td>
                    </tr>
                </tbody>
                </table>

                <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
                </div>
                </div>
                <!--[if (mso)|(IE)]></td><![endif]-->
                    <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
                    </div>
                </div>
                </div>



                <div class="u-row-container" style="padding: 0px;background-color: transparent">
                <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;">
                    <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                    <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #ffffff;"><![endif]-->
                    
                <!--[if (mso)|(IE)]><td align="center" width="600" style="width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
                <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                <div style="height: 100%;width: 100% !important;">
                <!--[if (!mso)&(!IE)]><!--><div style="height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
                
                <table id="u_content_image_2" style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                    <tr>
                    <td style="overflow-wrap:break-word;word-break:break-word;padding:15px 0px 10px;font-family:'Montserrat',sans-serif;" align="left">
                        
                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                    <td style="padding-right: 0px;padding-left: 0px;" align="center">
                    
                    <img align="center" border="0" src="cid:image5" alt="Hero Image" title="Hero Image" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 77%;max-width: 462px;" width="462" class="v-src-width v-src-max-width"/>
                    
                    </td>
                </tr>
                </table>

                    </td>
                    </tr>
                </tbody>
                </table>

                <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
                </div>
                </div>
                <!--[if (mso)|(IE)]></td><![endif]-->
                    <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
                    </div>
                </div>
                </div>



                <div class="u-row-container" style="padding: 0px;background-color: transparent">
                <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;">
                    <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                    <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #ffffff;"><![endif]-->
                    
                <!--[if (mso)|(IE)]><td align="center" width="600" style="width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
                <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                <div style="height: 100%;width: 100% !important;">
                <!--[if (!mso)&(!IE)]><!--><div style="height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
                
                <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                    <tr>
                    <td style="overflow-wrap:break-word;word-break:break-word;padding:0px 10px;font-family:'Montserrat',sans-serif;" align="left">
                        
                <h1 style="margin: 0px; color: #264653; line-height: 140%; text-align: center; word-wrap: break-word; font-weight: normal; font-family: arial,helvetica,sans-serif; font-size: 38px;">
                    <strong>Parab??ns!</strong>
                </h1>

                    </td>
                    </tr>
                </tbody>
                </table>

                <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                    <tr>
                    <td style="overflow-wrap:break-word;word-break:break-word;padding:0px 10px 20px;font-family:'Montserrat',sans-serif;" align="left">
                        
                <div style="line-height: 140%; text-align: center; word-wrap: break-word;">
                    <p style="font-size: 14px; line-height: 140%;"><span style="font-size: 22px; line-height: 30.8px; color: #2a9d8f;"><strong>Voc?? foi aceito(a).</strong></span></p>
                </div>

                    </td>
                    </tr>
                </tbody>
                </table>

                <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
                </div>
                </div>
                <!--[if (mso)|(IE)]></td><![endif]-->
                    <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
                    </div>
                </div>
                </div>



                <div class="u-row-container" style="padding: 0px;background-color: transparent">
                <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #bfedd2;">
                    <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                    <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #bfedd2;"><![endif]-->
                    
                <!--[if (mso)|(IE)]><td align="center" width="600" style="width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
                <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                <div style="height: 100%;width: 100% !important;">
                <!--[if (!mso)&(!IE)]><!--><div style="height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
                
                <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                    <tr>
                    <td style="overflow-wrap:break-word;word-break:break-word;padding:25px 10px 0px 30px;font-family:'Montserrat',sans-serif;" align="left">
                        
                <div style="color: #264653; line-height: 140%; text-align: left; word-wrap: break-word;">
                    <p style="line-height: 140%; font-size: 14px;"><span style="line-height: 19.6px; font-size: 14px;"><span style="font-size: 16px; line-height: 22.4px;"><strong>Ol??, voc??</strong></span><strong style="font-size: 16px;">, tudo bem???</strong></span></p>
                </div>

                    </td>
                    </tr>
                </tbody>
                </table>

                <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                    <tr>
                    <td style="overflow-wrap:break-word;word-break:break-word;padding:10px 30px;font-family:'Montserrat',sans-serif;" align="left">
                        
                <div style="color: #264653; line-height: 160%; text-align: left; word-wrap: break-word;">
                    <p style="font-size: 14px; line-height: 160%; text-align: justify;">Estou enviando esta resposta pois recebemos a sua hist??ria e temos o prazer de anunciar que <strong>aceitamos </strong>ela na <span style="text-decoration: underline; font-size: 14px; line-height: 22.4px;"><span style="color: #2dc26b; font-size: 14px; line-height: 22.4px; text-decoration: underline;">Kiniga</span></span>!</p>
                <p style="font-size: 14px; line-height: 160%; text-align: justify;">Pe??o que n??o pule esta mensagem, pois ela ?? de <strong>extrema import??ncia</strong> para que sua hist??ria seja publicada sem que ocorra nenhum problema.??</p>
                </div>

                    </td>
                    </tr>
                </tbody>
                </table>

                <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                    <tr>
                    <td style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 0px 30px;font-family:'Montserrat',sans-serif;" align="left">
                        
                <div style="color: #264653; line-height: 140%; text-align: left; word-wrap: break-word;">
                    <p style="font-size: 14px; line-height: 140%;"><strong>O que fazer</strong></p>
                </div>

                    </td>
                    </tr>
                </tbody>
                </table>

                <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                    <tr>
                    <td style="overflow-wrap:break-word;word-break:break-word;padding:0px 20px 10px 30px;font-family:'Montserrat',sans-serif;" align="left">
                        
                <div style="color: #264653; line-height: 180%; text-align: left; word-wrap: break-word;">
                    <p style="font-size: 14px; line-height: 180%; text-align: justify;">Supondo que voc?? j?? tenha lido todas as nossas <span style="color: #2dc26b; font-size: 14px; line-height: 25.2px;"><a rel="noopener" href="https://politicas.kiniga.com/" target="_blank" style="color: #2dc26b;">Pol??ticas</a></span>, que tamb??m ?? de extrema import??ncia, decidimos criar um <a rel="noopener" href="https://docs.google.com/document/d/1Yrj84cdIQQwFMkmCZ8k9YLgLkA4dngI57yl3TtfxqaE/edit?usp=sharing" target="_blank"><span style="color: #2dc26b; font-size: 14px; line-height: 25.2px;">FAQ</span></a>??para sanar qualquer d??vida relacionada ao processo de avalia????o e publica????o de hist??rias, bem como acontecimentos deste servidor, como s??o aplicadas puni????es, feitos os an??ncios, e mais. Fora isso, sugiro que siga as instru????es abaixo para que sua hist??ria n??o perca o lugar na fila de publica????o.??</p>
                </div>

                    </td>
                    </tr>
                </tbody>
                </table>

                <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                    <tr>
                    <td style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 0px 30px;font-family:'Montserrat',sans-serif;" align="left">
                        
                <div style="color: #264653; line-height: 140%; text-align: left; word-wrap: break-word;">
                    <p style="font-size: 14px; line-height: 140%;"><strong>N??o saia do servidor</strong></p>
                </div>

                    </td>
                    </tr>
                </tbody>
                </table>

                <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                    <tr>
                    <td style="overflow-wrap:break-word;word-break:break-word;padding:0px 20px 10px 30px;font-family:'Montserrat',sans-serif;" align="left">
                        
                <div style="color: #264653; line-height: 180%; text-align: left; word-wrap: break-word;">
                    <p style="font-size: 14px; line-height: 180%; text-align: justify;">Para que nosso sistema de publica????o funcione sem problemas, ?? preciso que o autor ou autora esteja no servidor. Assim, poderemos avis??-los do <strong>lan??amento</strong>, explicar como poder??o <strong>publicar </strong>seus cap??tulos, <strong>criar a tag</strong> da hist??ria e quais canais usar para coisas espec??ficas, como an??ncios sobre a hist??ria.</p>
                </div>

                    </td>
                    </tr>
                </tbody>
                </table>

                <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                    <tr>
                    <td style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 0px 30px;font-family:'Montserrat',sans-serif;" align="left">
                        
                <div style="color: #264653; line-height: 140%; text-align: left; word-wrap: break-word;">
                    <p style="font-size: 14px; line-height: 140%;"><strong>N??o mude o seu ID.</strong></p>
                </div>

                    </td>
                    </tr>
                </tbody>
                </table>

                <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                    <tr>
                    <td style="overflow-wrap:break-word;word-break:break-word;padding:0px 20px 10px 30px;font-family:'Montserrat',sans-serif;" align="left">
                        
                <div style="color: #264653; line-height: 180%; text-align: left; word-wrap: break-word;">
                    <p style="font-size: 14px; line-height: 180%; text-align: justify;">Com o mesmo objetivo de melhor funcionamento do sistema, pedimos para que n??o alterem seu ID do Discord ??? o mesmo que voc?? inseriu no formul??rio. Ex: Shuichi#6999</p>
                <p style="font-size: 14px; line-height: 180%; text-align: justify;">??</p>
                <p style="font-size: 14px; line-height: 180%; text-align: justify;">N??o estamos falando do seu <strong>apelido </strong>no servidor, mas sim seu ID. Ap??s a publica????o da sua hist??ria e se voc?? j?? tiver criado a TAG da sua hist??ria, voc?? poder?? alterar seu ID se desejar. Mas, at?? l??, pedimos que permane??a com o mesmo que foi inserido no formul??rio.</p>
                <p style="font-size: 14px; line-height: 180%; text-align: justify;">??</p>
                <p style="font-size: 14px; line-height: 180%; text-align: justify;"><span style="background-color: #c2e0f4; font-size: 14px; line-height: 25.2px;">Caso voc?? n??o tenha alternativa al??m dalterar seu ID, ou por algum motivo teve que mudar de conta, pedimos que marque o <strong>@Jonathan (O Budista)</strong> no canal <strong>?????chat-geral-s??rio</strong> contando seu problema em detalhes.??</span></p>
                </div>

                    </td>
                    </tr>
                </tbody>
                </table>

                <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                    <tr>
                    <td style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 0px 30px;font-family:'Montserrat',sans-serif;" align="left">
                        
                <div style="color: #264653; line-height: 140%; text-align: left; word-wrap: break-word;">
                    <p style="font-size: 14px; line-height: 140%;"><strong>Forne??a o link do cap??tulo corretamente.</strong></p>
                </div>

                    </td>
                    </tr>
                </tbody>
                </table>

                <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                    <tr>
                    <td style="overflow-wrap:break-word;word-break:break-word;padding:0px 20px 10px 30px;font-family:'Montserrat',sans-serif;" align="left">
                        
                <div style="color: #264653; line-height: 180%; text-align: left; word-wrap: break-word;">
                    <p style="font-size: 14px; line-height: 180%; text-align: justify;">Se a hist??ria for aceita, os Editores entram em contato solicitando o cap??tulo da hist??ria que ser?? publicado no lan??amento. Esse link deve ser o de um servi??o de armazenamento online, como o <span style="text-decoration: underline; font-size: 14px; line-height: 25.2px;">Google Drive</span>, <span style="text-decoration: underline; font-size: 14px; line-height: 25.2px;">One Drive</span>, <span style="text-decoration: underline; font-size: 14px; line-height: 25.2px;">Dropbox</span>, etc. ?? <strong>essencial </strong>que o Editor(a) possa acessar o arquivo para que ele(a) possa publicar a hist??ria, e se o arquivo n??o estiver com a op????o de compartilhamento com, pelo menos, <strong>permiss??o para ler</strong>, isso n??o ser?? poss??vel.??</p>
                </div>

                    </td>
                    </tr>
                </tbody>
                </table>

                <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                    <tr>
                    <td style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 0px 30px;font-family:'Montserrat',sans-serif;" align="left">
                        
                <div style="color: #264653; line-height: 140%; text-align: left; word-wrap: break-word;">
                    <p style="font-size: 14px; line-height: 140%;"><strong>Consequ??ncia.</strong></p>
                </div>

                    </td>
                    </tr>
                </tbody>
                </table>

                <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                    <tr>
                    <td style="overflow-wrap:break-word;word-break:break-word;padding:0px 20px 10px 30px;font-family:'Montserrat',sans-serif;" align="left">
                        
                <div style="color: #264653; line-height: 180%; text-align: left; word-wrap: break-word;">
                    <p style="font-size: 14px; line-height: 180%; text-align: justify;">Se qualquer uma das coisas acima acontecer, a sua hist??ria perder?? o lugar na fila. O que significa que, quando algum Editor tentar public??-la e n??o for poss??vel, sua hist??ria passar?? a ser a ??ltima a ser publicada. Portanto, mantenha isso em mente e tente n??o bobear. Caso tenha sido reportado ?? um Editor/Administrador, e o problema tenha sido solucionado, n??o haver?? consequ??ncia.??</p>
                </div>

                    </td>
                    </tr>
                </tbody>
                </table>

                <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                    <tr>
                    <td style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 0px 30px;font-family:'Montserrat',sans-serif;" align="left">
                        
                <div style="color: #264653; line-height: 140%; text-align: left; word-wrap: break-word;">
                    <p style="font-size: 14px; line-height: 140%;"><span style="font-size: 14px; line-height: 19.6px; background-color: #f8cac6;"><strong>ATEN????O!</strong></span></p>
                </div>

                    </td>
                    </tr>
                </tbody>
                </table>

                <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                    <tr>
                    <td style="overflow-wrap:break-word;word-break:break-word;padding:0px 20px 10px 30px;font-family:'Montserrat',sans-serif;" align="left">
                        
                <div style="color: #264653; line-height: 180%; text-align: left; word-wrap: break-word;">
                    <p style="font-size: 14px; line-height: 180%; text-align: justify;"><span style="background-color: #f8cac6; font-size: 14px; line-height: 25.2px;">Todas as suas d??vidas, e mais, podem ser </span><span style="background-color: #f8cac6; font-size: 14px; line-height: 25.2px;">respondidas ao ler o FAQ.??</span></p>
                </div>

                    </td>
                    </tr>
                </tbody>
                </table>

                <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                    <tr>
                    <td style="overflow-wrap:break-word;word-break:break-word;padding:10px 30px;font-family:'Montserrat',sans-serif;" align="left">
                        
                <div style="color: #264653; line-height: 160%; text-align: left; word-wrap: break-word;">
                    <p style="font-size: 14px; line-height: 160%;"><strong><span style="font-family: Lato, sans-serif; font-size: 14px; line-height: 22.4px; color: #264653;">Se voc?? tiver alguma d??vida, contate-nos pelo Discord.<span style="color: #34495e; font-size: 14px; line-height: 22.4px;"></span></span></strong></p>
                </div>

                    </td>
                    </tr>
                </tbody>
                </table>

                <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
                </div>
                </div>
                <!--[if (mso)|(IE)]></td><![endif]-->
                    <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
                    </div>
                </div>
                </div>



                <div class="u-row-container" style="padding: 0px;background-color: transparent">
                <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #264653;">
                    <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                    <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #264653;"><![endif]-->
                    
                <!--[if (mso)|(IE)]><td align="center" width="600" style="width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
                <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                <div style="height: 100%;width: 100% !important;">
                <!--[if (!mso)&(!IE)]><!--><div style="height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
                
                <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                    <tr>
                    <td style="overflow-wrap:break-word;word-break:break-word;padding:30px 10px 0px;font-family:'Montserrat',sans-serif;" align="left">
                        
                <h1 style="margin: 0px; color: #ffffff; line-height: 140%; text-align: center; word-wrap: break-word; font-weight: normal; font-family: trebuchet ms,geneva; font-size: 22px;">
                    <strong>Sobre N??s</strong>
                </h1>

                    </td>
                    </tr>
                </tbody>
                </table>

                <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                    <tr>
                    <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Montserrat',sans-serif;" align="left">
                        
                <div style="line-height: 140%; text-align: center; word-wrap: break-word;">
                    <p style="font-size: 14px; line-height: 140%;"><span style="color: #ffffff; font-size: 14px; line-height: 19.6px;">W W W . K I N I G A . C O M</span></p>
                </div>

                    </td>
                    </tr>
                </tbody>
                </table>

                <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                    <tr>
                    <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Montserrat',sans-serif;" align="left">
                        
                <div align="center">
                <div style="display: table; max-width:167px;">
                <!--[if (mso)|(IE)]><table width="167" cellpadding="0" cellspacing="0" border="0"><tr><td style="border-collapse:collapse;" align="center"><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse; mso-table-lspace: 0pt;mso-table-rspace: 0pt; width:167px;"><tr><![endif]-->
                
                    
                    <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 10px;" valign="top"><![endif]-->
                    <table align="left" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 10px">
                    <tbody><tr style="vertical-align: top"><td align="left" valign="middle" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                        <a href="https://www.facebook.com/kinigabrasil" title="Facebook" target="_blank">
                        <img src="cid:image1" alt="Facebook" title="Facebook" width="32" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
                        </a>
                    </td></tr>
                    </tbody></table>
                    <!--[if (mso)|(IE)]></td><![endif]-->
                    
                    <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 10px;" valign="top"><![endif]-->
                    <table align="left" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 10px">
                    <tbody><tr style="vertical-align: top"><td align="left" valign="middle" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                        <a href="https://twitter.com/KinigaBrasil" title="Twitter" target="_blank">
                        <img src="cid:image2" alt="Twitter" title="Twitter" width="32" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
                        </a>
                    </td></tr>
                    </tbody></table>
                    <!--[if (mso)|(IE)]></td><![endif]-->
                    
                    <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 10px;" valign="top"><![endif]-->
                    <table align="left" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 10px">
                    <tbody><tr style="vertical-align: top"><td align="left" valign="middle" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                        <a href="https://www.instagram.com/p/CAp_qaQHEuM/" title="Instagram" target="_blank">
                        <img src="cid:image4" alt="Instagram" title="Instagram" width="32" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
                        </a>
                    </td></tr>
                    </tbody></table>
                    <!--[if (mso)|(IE)]></td><![endif]-->
                    
                    <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 0px;" valign="top"><![endif]-->
                    <table align="left" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 0px">
                    <tbody><tr style="vertical-align: top"><td align="left" valign="middle" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                        <a href="https://discord.gg/QMKHU8y" title="Discord" target="_blank">
                        <img src="cid:image6" alt="Discord" title="Discord" width="32" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
                        </a>
                    </td></tr>
                    </tbody></table>
                    <!--[if (mso)|(IE)]></td><![endif]-->
                    
                    
                    <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
                </div>
                </div>

                    </td>
                    </tr>
                </tbody>
                </table>

                <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                    <tr>
                    <td style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 15px;font-family:'Montserrat',sans-serif;" align="left">
                        
                <div style="color: #ffffff; line-height: 160%; text-align: center; word-wrap: break-word;">
                    <p style="font-size: 14px; line-height: 160%;">????? 2022 ??? Todos os direitos reservados<br /><span style="color: #ffffff; font-size: 14px; line-height: 22.4px;"><a rel="noopener" href="https://politicas.kiniga.com/termos-de-servico/" target="_blank" style="color: #ffffff;">Termos de Servi??o</a></span> | <span style="color: #ffffff; font-size: 14px; line-height: 22.4px;"><a rel="noopener" href="https://politicas.kiniga.com/politicas-de-privacidade/" target="_blank" style="color: #ffffff;">Pol??tica de Privacidade</a></span></p>
                </div>

                    </td>
                    </tr>
                </tbody>
                </table>

                <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
                </div>
                </div>
                <!--[if (mso)|(IE)]></td><![endif]-->
                    <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
                    </div>
                </div>
                </div>


                    <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                    </td>
                </tr>
                </tbody>
                </table>
                <!--[if mso]></div><![endif]-->
                <!--[if IE]></div><![endif]-->
                </body>

                </html>


            """
            emailtxt = """\
                
                ESTA ?? UMA MENSAGEM AUTOM??TICA. N??O RESPONDA.
                
                Ol??, voc??, tudo bem? 

                Estou enviando esta resposta pois recebemos a sua hist??ria e temos o prazer de anunciar que aceitamos ela na Kiniga!

                Pe??o que n??o pule esta mensagem, pois ela ?? de extrema import??ncia para que sua hist??ria seja publicada sem que ocorra nenhum problema. 

                O que fazer

                Supondo que voc?? j?? tenha lido todas as nossas Pol??ticas (https://politicas.kiniga.com/), que tamb??m ?? de extrema import??ncia, decidimos criar um FAQ (https://docs.google.com/document/d/1Yrj84cdIQQwFMkmCZ8k9YLgLkA4dngI57yl3TtfxqaE/edit?usp=sharing) para sanar qualquer d??vida relacionada ao processo de avalia????o e publica????o de hist??rias, bem como acontecimentos de nosso servidor, como s??o aplicadas puni????es, feitos os an??ncios, e mais. Fora isso, sugiro que siga as instru????es abaixo para que sua hist??ria n??o perca o lugar na fila de publica????o. 

                N??o saia do servidor

                Para que nosso sistema de publica????o funcione sem problemas, ?? preciso que o autor ou autora esteja no servidor. Assim, poderemos avis??-los do lan??amento, explicar como poder??o publicar seus cap??tulos, criar a tag da hist??ria e quais canais usar para coisas espec??ficas, como an??ncios sobre a hist??ria.

                N??o mude o seu ID.

                Com o mesmo objetivo de melhor funcionamento do sistema, pedimos para que n??o alterem seu ID do Discord ??? o mesmo que voc?? inseriu no formul??rio. Ex: Shuichi#6996

                

                N??o estamos falando do seu apelido no servidor, mas sim seu ID. Ap??s a publica????o da sua hist??ria e se voc?? j?? tiver criado a TAG da sua hist??ria, voc?? poder?? alterar seu ID se desejar. Mas, at?? l??, pedimos que permane??a com o mesmo que foi inserido no formul??rio.

                

                Caso voc?? n??o tenha alternativa al??m de alterar seu ID, ou por algum motivo teve que mudar de conta, pedimos que marque o @Jonathan (O Budista) no canal ?????chat-geral-s??rio contando seu problema em detalhes. 

                Forne??a o link do cap??tulo corretamente.

                Se a hist??ria for aceita, os Editores entram em contato solicitando o cap??tulo da hist??ria que ser?? publicado no lan??amento. Esse link deve ser o de um servi??o de armazenamento online, como o Google Drive, One Drive, Dropbox, etc. ?? essencial que o Editor(a) possa acessar o arquivo para que ele(a) possa publicar a hist??ria, e se o arquivo n??o estiver com a op????o de compartilhamento com, pelo menos, permiss??o para ler, isso n??o ser?? poss??vel. 

                Consequ??ncia.

                Se qualquer uma das coisas acima acontecer, a sua hist??ria perder?? o lugar na fila. O que significa que, quando algum Editor tentar public??-la e n??o for poss??vel, sua hist??ria passar?? a ser a ??ltima a ser publicada. Portanto, mantenha isso em mente e tente n??o bobear. Caso tenha sido reportado ?? um Editor/Administrador, e o problema tenha sido solucionado, n??o haver?? consequ??ncia. 

                ATEN????O!

                Todas essas informa????es, e mais, podem ser
                encontradas no FAQ. Ent??o, mesmo que n??o consiga ler esta mensagem novamente, voc?? ainda poder?? essas informa????es l??. 

                Se voc?? tiver alguma d??vida, contate-nos pelo Discord.

                Att,
                Equipe Kiniga Brasil.
                
            """
        elif status == 'refuse':
            email = """\
                <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
                <html
                xmlns="http://www.w3.org/1999/xhtml"
                xmlns:v="urn:schemas-microsoft-com:vml"
                xmlns:o="urn:schemas-microsoft-com:office:office"
                >
                <head>
                    <!--[if gte mso 9]>
                    <xml>
                        <o:OfficeDocumentSettings>
                        <o:AllowPNG />
                        <o:PixelsPerInch>96</o:PixelsPerInch>
                        </o:OfficeDocumentSettings>
                    </xml>
                    <![endif]-->
                    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                    <meta name="x-apple-disable-message-reformatting" />
                    <!--[if !mso]><!-->
                    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                    <!--<![endif]-->
                    <title></title>

                    <style type="text/css">
                    @media only screen and (min-width: 620px) {
                        .u-row {
                        width: 600px !important;
                        }

                        .u-row .u-col {
                        vertical-align: top;
                        }

                        .u-row .u-col-100 {
                        width: 600px !important;
                        }
                    }

                    @media (max-width: 620px) {
                        .u-row-container {
                        max-width: 100% !important;
                        padding-left: 0px !important;
                        padding-right: 0px !important;
                        }

                        .u-row .u-col {
                        min-width: 320px !important;
                        max-width: 100% !important;
                        display: block !important;
                        }

                        .u-row {
                        width: calc(100% - 40px) !important;
                        }

                        .u-col {
                        width: 100% !important;
                        }

                        .u-col > div {
                        margin: 0 auto;
                        }
                    }

                    body {
                        margin: 0;
                        padding: 0;
                    }

                    table,
                    tr,
                    td {
                        vertical-align: top;
                        border-collapse: collapse;
                    }

                    p {
                        margin: 0;
                    }

                    .ie-container table,
                    .mso-container table {
                        table-layout: fixed;
                    }

                    * {
                        line-height: inherit;
                    }

                    a[x-apple-data-detectors="true"] {
                        color: inherit !important;
                        text-decoration: none !important;
                    }

                    table,
                    td {
                        color: #000000;
                    }

                    #u_body a {
                        color: #0000ee;
                        text-decoration: underline;
                    }

                    @media (max-width: 480px) {
                        #u_content_image_1 .v-src-width {
                        width: auto !important;
                        }

                        #u_content_image_1 .v-src-max-width {
                        max-width: 38% !important;
                        }

                        #u_content_image_2 .v-src-width {
                        width: auto !important;
                        }

                        #u_content_image_2 .v-src-max-width {
                        max-width: 100% !important;
                        }
                    }
                    </style>

                    <!--[if !mso]><!-->
                    <link
                    href="https://fonts.googleapis.com/css?family=Lato:400,700&display=swap"
                    rel="stylesheet"
                    type="text/css"
                    />
                    <link
                    href="https://fonts.googleapis.com/css?family=Montserrat:400,700&display=swap"
                    rel="stylesheet"
                    type="text/css"
                    />
                    <!--<![endif]-->
                </head>

                <body
                    class="clean-body u_body"
                    style="
                    margin: 0;
                    padding: 0;
                    -webkit-text-size-adjust: 100%;
                    background-color: #ecf0f1;
                    color: #000000;
                    "
                >
                    <!--[if IE]><div class="ie-container"><![endif]-->
                    <!--[if mso]><div class="mso-container"><![endif]-->
                    <table
                    id="u_body"
                    style="
                        border-collapse: collapse;
                        table-layout: fixed;
                        border-spacing: 0;
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        vertical-align: top;
                        min-width: 320px;
                        margin: 0 auto;
                        background-color: #ecf0f1;
                        width: 100%;
                    "
                    cellpadding="0"
                    cellspacing="0"
                    >
                    <tbody>
                        <tr style="vertical-align: top">
                        <td
                            style="
                            word-break: break-word;
                            border-collapse: collapse !important;
                            vertical-align: top;
                            "
                        >
                            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #ecf0f1;"><![endif]-->

                            <div
                            class="u-row-container"
                            style="padding: 0px; background-color: transparent"
                            >
                            <div
                                class="u-row"
                                style="
                                margin: 0 auto;
                                min-width: 320px;
                                max-width: 600px;
                                overflow-wrap: break-word;
                                word-wrap: break-word;
                                word-break: break-word;
                                background-color: #264653;
                                "
                            >
                                <div
                                style="
                                    border-collapse: collapse;
                                    display: table;
                                    width: 100%;
                                    height: 100%;
                                    background-color: transparent;
                                "
                                >
                                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #264653;"><![endif]-->

                                <!--[if (mso)|(IE)]><td align="center" width="600" style="width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
                                <div
                                    class="u-col u-col-100"
                                    style="
                                    max-width: 320px;
                                    min-width: 600px;
                                    display: table-cell;
                                    vertical-align: top;
                                    "
                                >
                                    <div style="height: 100%; width: 100% !important">
                                    <!--[if (!mso)&(!IE)]><!-->
                                    <div
                                        style="
                                        height: 100%;
                                        padding: 0px;
                                        border-top: 0px solid transparent;
                                        border-left: 0px solid transparent;
                                        border-right: 0px solid transparent;
                                        border-bottom: 0px solid transparent;
                                        "
                                    >
                                        <!--<![endif]-->
                                        <table
                                        id="u_content_image_1"
                                        style="font-family: 'Montserrat', sans-serif"
                                        role="presentation"
                                        cellpadding="0"
                                        cellspacing="0"
                                        width="100%"
                                        border="0"
                                        >
                                        <tbody>
                                            <tr>
                                            <td
                                                style="
                                                overflow-wrap: break-word;
                                                word-break: break-word;
                                                padding: 20px 10px;
                                                font-family: 'Montserrat', sans-serif;
                                                "
                                                align="left"
                                            >
                                                <table
                                                width="100%"
                                                cellpadding="0"
                                                cellspacing="0"
                                                border="0"
                                                >
                                                <tr>
                                                    <td
                                                    style="
                                                        padding-right: 0px;
                                                        padding-left: 0px;
                                                    "
                                                    align="center"
                                                    >
                                                    <a
                                                        href="https://kiniga.com/"
                                                        target="_blank"
                                                    >
                                                        <img
                                                        align="center"
                                                        border="0"
                                                        src="cid:image3"
                                                        alt="Logo"
                                                        title="Logo"
                                                        style="
                                                            outline: none;
                                                            text-decoration: none;
                                                            -ms-interpolation-mode: bicubic;
                                                            clear: both;
                                                            display: inline-block !important;
                                                            border: none;
                                                            height: auto;
                                                            float: none;
                                                            width: 21%;
                                                            max-width: 121.8px;
                                                        "
                                                        width="121.8"
                                                        class="v-src-width v-src-max-width"
                                                        />
                                                    </a>
                                                    </td>
                                                </tr>
                                                </table>
                                            </td>
                                            </tr>
                                        </tbody>
                                        </table>

                                        <!--[if (!mso)&(!IE)]><!-->
                                    </div>
                                    <!--<![endif]-->
                                    </div>
                                </div>
                                <!--[if (mso)|(IE)]></td><![endif]-->
                                <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
                                </div>
                            </div>
                            </div>

                            <div
                            class="u-row-container"
                            style="padding: 0px; background-color: transparent"
                            ></div>

                            <div
                            class="u-row-container"
                            style="padding: 0px; background-color: transparent"
                            >
                            <div
                                class="u-row"
                                style="
                                margin: 0 auto;
                                min-width: 320px;
                                max-width: 600px;
                                overflow-wrap: break-word;
                                word-wrap: break-word;
                                word-break: break-word;
                                background-color: #ffffff;
                                "
                            >
                                <div
                                style="
                                    border-collapse: collapse;
                                    display: table;
                                    width: 100%;
                                    height: 100%;
                                    background-color: transparent;
                                "
                                >
                                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #ffffff;"><![endif]-->

                                <!--[if (mso)|(IE)]><td align="center" width="600" style="width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->

                                <!--[if (mso)|(IE)]></td><![endif]-->
                                <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
                                </div>
                            </div>
                            </div>

                            <div
                            class="u-row-container"
                            style="padding: 0px; background-color: transparent"
                            >
                            <div
                                class="u-row"
                                style="
                                margin: 0 auto;
                                min-width: 320px;
                                max-width: 600px;
                                overflow-wrap: break-word;
                                word-wrap: break-word;
                                word-break: break-word;
                                background-color: #bfedd2;
                                "
                            >
                                <div
                                style="
                                    border-collapse: collapse;
                                    display: table;
                                    width: 100%;
                                    height: 100%;
                                    background-color: transparent;
                                "
                                >
                                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #bfedd2;"><![endif]-->

                                <!--[if (mso)|(IE)]><td align="center" width="600" style="width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
                                <div
                                    class="u-col u-col-100"
                                    style="
                                    max-width: 320px;
                                    min-width: 600px;
                                    display: table-cell;
                                    vertical-align: top;
                                    "
                                >
                                    <div style="height: 100%; width: 100% !important">
                                    <!--[if (!mso)&(!IE)]><!-->
                                    <div
                                        style="
                                        height: 100%;
                                        padding: 0px;
                                        border-top: 0px solid transparent;
                                        border-left: 0px solid transparent;
                                        border-right: 0px solid transparent;
                                        border-bottom: 0px solid transparent;
                                        "
                                    >
                                        <!--<![endif]-->
                                        <table
                                        style="font-family: 'Montserrat', sans-serif"
                                        role="presentation"
                                        cellpadding="0"
                                        cellspacing="0"
                                        width="100%"
                                        border="0"
                                        >
                                        <tbody>
                                            <tr>
                                            <td
                                                style="
                                                overflow-wrap: break-word;
                                                word-break: break-word;
                                                padding: 25px 10px 0px 30px;
                                                font-family: 'Montserrat', sans-serif;
                                                "
                                                align="left"
                                            >
                                                <div
                                                style="
                                                    color: #264653;
                                                    line-height: 140%;
                                                    text-align: left;
                                                    word-wrap: break-word;
                                                "
                                                >
                                                <p style="line-height: 140%; font-size: 14px">
                                                    <span
                                                    style="
                                                        line-height: 19.6px;
                                                        font-size: 14px;
                                                    "
                                                    ><span
                                                        style="
                                                        font-size: 16px;
                                                        line-height: 22.4px;
                                                        "
                                                        ><strong>Ol??, voc??</strong></span
                                                    ><strong style="font-size: 16px"
                                                        >, tudo bem???</strong
                                                    ></span
                                                    >
                                                </p>
                                                </div>
                                            </td>
                                            </tr>
                                        </tbody>
                                        </table>

                                        <table
                                        style="font-family: 'Montserrat', sans-serif"
                                        role="presentation"
                                        cellpadding="0"
                                        cellspacing="0"
                                        width="100%"
                                        border="0"
                                        >
                                        <tbody>
                                            <tr>
                                            <td
                                                style="
                                                overflow-wrap: break-word;
                                                word-break: break-word;
                                                padding: 10px 30px;
                                                font-family: 'Montserrat', sans-serif;
                                                "
                                                align="left"
                                            >
                                                <div
                                                style="
                                                    color: #264653;
                                                    line-height: 160%;
                                                    text-align: left;
                                                    word-wrap: break-word;
                                                "
                                                >
                                                <p
                                                    style="
                                                    font-size: 14px;
                                                    line-height: 160%;
                                                    text-align: justify;
                                                    "
                                                >
                                                    Estou enviando esta resposta pois recebemos
                                                    a sua hist??ria, por??m ela foi recusada
                                                    na
                                                    <span
                                                    style="
                                                        text-decoration: underline;
                                                        font-size: 14px;
                                                        line-height: 22.4px;
                                                    "
                                                    ><span
                                                        style="
                                                        color: #2dc26b;
                                                        font-size: 14px;
                                                        line-height: 22.4px;
                                                        text-decoration: underline;
                                                        "
                                                        >Kiniga</span
                                                    ></span
                                                    >.
                                                </p>

                                                
                                                </div>
                                            </td>
                                            </tr>
                                        </tbody>
                                        </table>

                                        <br />

                                        <table
                                        style="font-family: 'Montserrat', sans-serif"
                                        role="presentation"
                                        cellpadding="0"
                                        cellspacing="0"
                                        width="100%"
                                        border="0"
                                        >
                                        <tbody>
                                            <tr>
                                            <td
                                                style="
                                                overflow-wrap: break-word;
                                                word-break: break-word;
                                                padding: 10px 10px 0px 30px;
                                                font-family: 'Montserrat', sans-serif;
                                                "
                                                align="left"
                                            >
                                                <div
                                                style="
                                                    color: #264653;
                                                    line-height: 140%;
                                                    text-align: left;
                                                    word-wrap: break-word;
                                                "
                                                >
                                                <p style="font-size: 14px; line-height: 140%">
                                                    <span
                                                    style="
                                                        font-size: 14px;
                                                        line-height: 19.6px;
                                                        background-color: #f8cac6;
                                                    "
                                                    ><strong>ATEN????O!</strong></span
                                                    >
                                                </p>
                                                </div>
                                            </td>
                                            </tr>
                                        </tbody>
                                        </table>

                                        <table
                                        style="font-family: 'Montserrat', sans-serif"
                                        role="presentation"
                                        cellpadding="0"
                                        cellspacing="0"
                                        width="100%"
                                        border="0"
                                        >
                                        <tbody>
                                            <tr>
                                            <td
                                                style="
                                                overflow-wrap: break-word;
                                                word-break: break-word;
                                                padding: 0px 20px 10px 30px;
                                                font-family: 'Montserrat', sans-serif;
                                                "
                                                align="left"
                                            >
                                                <div
                                                style="
                                                    color: #264653;
                                                    line-height: 180%;
                                                    text-align: left;
                                                    word-wrap: break-word;
                                                "
                                                >
                                                <p
                                                    style="
                                                    font-size: 14px;
                                                    line-height: 180%;
                                                    text-align: justify;
                                                    "
                                                >
                                                    <span
                                                    style="
                                                        background-color: #f8cac6;
                                                        font-size: 14px;
                                                        line-height: 25.2px;
                                                    "
                                                    >Todas as suas d??vidas, e mais, podem
                                                    ser</span
                                                    ><span
                                                    style="
                                                        background-color: #f8cac6;
                                                        font-size: 14px;
                                                        line-height: 25.2px;
                                                    "
                                                    >respondidas ao ler o
                                                    <a
                                                        rel="noopener"
                                                        href="https://docs.google.com/document/d/1Yrj84cdIQQwFMkmCZ8k9YLgLkA4dngI57yl3TtfxqaE/edit?usp=sharing"
                                                        target="_blank"
                                                        ><span
                                                        style="
                                                            color: #2dc26b;
                                                            font-size: 14px;
                                                            line-height: 25.2px;
                                                        "
                                                        >FAQ</span
                                                        ></a
                                                    >.??</span
                                                    >
                                                </p>
                                                </div>
                                            </td>
                                            </tr>
                                        </tbody>
                                        </table>

                                        <table
                                        style="font-family: 'Montserrat', sans-serif"
                                        role="presentation"
                                        cellpadding="0"
                                        cellspacing="0"
                                        width="100%"
                                        border="0"
                                        >
                                        <tbody>
                                            <tr>
                                            <td
                                                style="
                                                overflow-wrap: break-word;
                                                word-break: break-word;
                                                padding: 10px 30px;
                                                font-family: 'Montserrat', sans-serif;
                                                "
                                                align="left"
                                            >
                                                <div
                                                style="
                                                    color: #264653;
                                                    line-height: 160%;
                                                    text-align: left;
                                                    word-wrap: break-word;
                                                "
                                                >
                                                <p style="font-size: 14px; line-height: 160%">
                                                    <strong
                                                    ><span
                                                        style="
                                                        font-family: Lato, sans-serif;
                                                        font-size: 14px;
                                                        line-height: 22.4px;
                                                        color: #264653;
                                                        "
                                                        >Mas, se voc?? tiver alguma d??vida,
                                                        contate-nos pelo Discord.<span
                                                        style="
                                                            color: #34495e;
                                                            font-size: 14px;
                                                            line-height: 22.4px;
                                                        "
                                                        ></span></span
                                                    ></strong>
                                                </p>
                                                </div>
                                            </td>
                                            </tr>
                                        </tbody>
                                        </table>

                                        <!--[if (!mso)&(!IE)]><!-->
                                    </div>
                                    <!--<![endif]-->
                                    </div>
                                </div>
                                <!--[if (mso)|(IE)]></td><![endif]-->
                                <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
                                </div>
                            </div>
                            </div>

                            <div
                            class="u-row-container"
                            style="padding: 0px; background-color: transparent"
                            >
                            <div
                                class="u-row"
                                style="
                                margin: 0 auto;
                                min-width: 320px;
                                max-width: 600px;
                                overflow-wrap: break-word;
                                word-wrap: break-word;
                                word-break: break-word;
                                background-color: #264653;
                                "
                            >
                                <div
                                style="
                                    border-collapse: collapse;
                                    display: table;
                                    width: 100%;
                                    height: 100%;
                                    background-color: transparent;
                                "
                                >
                                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #264653;"><![endif]-->

                                <!--[if (mso)|(IE)]><td align="center" width="600" style="width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
                                <div
                                    class="u-col u-col-100"
                                    style="
                                    max-width: 320px;
                                    min-width: 600px;
                                    display: table-cell;
                                    vertical-align: top;
                                    "
                                >
                                    <div style="height: 100%; width: 100% !important">
                                    <!--[if (!mso)&(!IE)]><!-->
                                    <div
                                        style="
                                        height: 100%;
                                        padding: 0px;
                                        border-top: 0px solid transparent;
                                        border-left: 0px solid transparent;
                                        border-right: 0px solid transparent;
                                        border-bottom: 0px solid transparent;
                                        "
                                    >
                                        <!--<![endif]-->
                                        <table
                                        style="font-family: 'Montserrat', sans-serif"
                                        role="presentation"
                                        cellpadding="0"
                                        cellspacing="0"
                                        width="100%"
                                        border="0"
                                        >
                                        <tbody>
                                            <tr>
                                            <td
                                                style="
                                                overflow-wrap: break-word;
                                                word-break: break-word;
                                                padding: 30px 10px 0px;
                                                font-family: 'Montserrat', sans-serif;
                                                "
                                                align="left"
                                            >
                                                <h1
                                                style="
                                                    margin: 0px;
                                                    color: #ffffff;
                                                    line-height: 140%;
                                                    text-align: center;
                                                    word-wrap: break-word;
                                                    font-weight: normal;
                                                    font-family: trebuchet ms, geneva;
                                                    font-size: 22px;
                                                "
                                                >
                                                <strong>Sobre N??s</strong>
                                                </h1>
                                            </td>
                                            </tr>
                                        </tbody>
                                        </table>

                                        <table
                                        style="font-family: 'Montserrat', sans-serif"
                                        role="presentation"
                                        cellpadding="0"
                                        cellspacing="0"
                                        width="100%"
                                        border="0"
                                        >
                                        <tbody>
                                            <tr>
                                            <td
                                                style="
                                                overflow-wrap: break-word;
                                                word-break: break-word;
                                                padding: 10px;
                                                font-family: 'Montserrat', sans-serif;
                                                "
                                                align="left"
                                            >
                                                <div
                                                style="
                                                    line-height: 140%;
                                                    text-align: center;
                                                    word-wrap: break-word;
                                                "
                                                >
                                                <p style="font-size: 14px; line-height: 140%">
                                                    <span
                                                    style="
                                                        color: #ffffff;
                                                        font-size: 14px;
                                                        line-height: 19.6px;
                                                    "
                                                    >W W W . K I N I G A . C O M</span
                                                    >
                                                </p>
                                                </div>
                                            </td>
                                            </tr>
                                        </tbody>
                                        </table>

                                        <table
                                        style="font-family: 'Montserrat', sans-serif"
                                        role="presentation"
                                        cellpadding="0"
                                        cellspacing="0"
                                        width="100%"
                                        border="0"
                                        >
                                        <tbody>
                                            <tr>
                                            <td
                                                style="
                                                overflow-wrap: break-word;
                                                word-break: break-word;
                                                padding: 10px;
                                                font-family: 'Montserrat', sans-serif;
                                                "
                                                align="left"
                                            >
                                                <div align="center">
                                                <div style="display: table; max-width: 167px">
                                                    <!--[if (mso)|(IE)]><table width="167" cellpadding="0" cellspacing="0" border="0"><tr><td style="border-collapse:collapse;" align="center"><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse; mso-table-lspace: 0pt;mso-table-rspace: 0pt; width:167px;"><tr><![endif]-->

                                                    <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 10px;" valign="top"><![endif]-->
                                                    <table
                                                    align="left"
                                                    border="0"
                                                    cellspacing="0"
                                                    cellpadding="0"
                                                    width="32"
                                                    height="32"
                                                    style="
                                                        width: 32px !important;
                                                        height: 32px !important;
                                                        display: inline-block;
                                                        border-collapse: collapse;
                                                        table-layout: fixed;
                                                        border-spacing: 0;
                                                        mso-table-lspace: 0pt;
                                                        mso-table-rspace: 0pt;
                                                        vertical-align: top;
                                                        margin-right: 10px;
                                                    "
                                                    >
                                                    <tbody>
                                                        <tr style="vertical-align: top">
                                                        <td
                                                            align="left"
                                                            valign="middle"
                                                            style="
                                                            word-break: break-word;
                                                            border-collapse: collapse !important;
                                                            vertical-align: top;
                                                            "
                                                        >
                                                            <a
                                                            href="https://www.facebook.com/kinigabrasil"
                                                            title="Facebook"
                                                            target="_blank"
                                                            >
                                                            <img
                                                                src="cid:image1"
                                                                alt="Facebook"
                                                                title="Facebook"
                                                                width="32"
                                                                style="
                                                                outline: none;
                                                                text-decoration: none;
                                                                -ms-interpolation-mode: bicubic;
                                                                clear: both;
                                                                display: block !important;
                                                                border: none;
                                                                height: auto;
                                                                float: none;
                                                                max-width: 32px !important;
                                                                "
                                                            />
                                                            </a>
                                                        </td>
                                                        </tr>
                                                    </tbody>
                                                    </table>
                                                    <!--[if (mso)|(IE)]></td><![endif]-->

                                                    <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 10px;" valign="top"><![endif]-->
                                                    <table
                                                    align="left"
                                                    border="0"
                                                    cellspacing="0"
                                                    cellpadding="0"
                                                    width="32"
                                                    height="32"
                                                    style="
                                                        width: 32px !important;
                                                        height: 32px !important;
                                                        display: inline-block;
                                                        border-collapse: collapse;
                                                        table-layout: fixed;
                                                        border-spacing: 0;
                                                        mso-table-lspace: 0pt;
                                                        mso-table-rspace: 0pt;
                                                        vertical-align: top;
                                                        margin-right: 10px;
                                                    "
                                                    >
                                                    <tbody>
                                                        <tr style="vertical-align: top">
                                                        <td
                                                            align="left"
                                                            valign="middle"
                                                            style="
                                                            word-break: break-word;
                                                            border-collapse: collapse !important;
                                                            vertical-align: top;
                                                            "
                                                        >
                                                            <a
                                                            href="https://twitter.com/KinigaBrasil"
                                                            title="Twitter"
                                                            target="_blank"
                                                            >
                                                            <img
                                                                src="cid:image2"
                                                                alt="Twitter"
                                                                title="Twitter"
                                                                width="32"
                                                                style="
                                                                outline: none;
                                                                text-decoration: none;
                                                                -ms-interpolation-mode: bicubic;
                                                                clear: both;
                                                                display: block !important;
                                                                border: none;
                                                                height: auto;
                                                                float: none;
                                                                max-width: 32px !important;
                                                                "
                                                            />
                                                            </a>
                                                        </td>
                                                        </tr>
                                                    </tbody>
                                                    </table>
                                                    <!--[if (mso)|(IE)]></td><![endif]-->

                                                    <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 10px;" valign="top"><![endif]-->
                                                    <table
                                                    align="left"
                                                    border="0"
                                                    cellspacing="0"
                                                    cellpadding="0"
                                                    width="32"
                                                    height="32"
                                                    style="
                                                        width: 32px !important;
                                                        height: 32px !important;
                                                        display: inline-block;
                                                        border-collapse: collapse;
                                                        table-layout: fixed;
                                                        border-spacing: 0;
                                                        mso-table-lspace: 0pt;
                                                        mso-table-rspace: 0pt;
                                                        vertical-align: top;
                                                        margin-right: 10px;
                                                    "
                                                    >
                                                    <tbody>
                                                        <tr style="vertical-align: top">
                                                        <td
                                                            align="left"
                                                            valign="middle"
                                                            style="
                                                            word-break: break-word;
                                                            border-collapse: collapse !important;
                                                            vertical-align: top;
                                                            "
                                                        >
                                                            <a
                                                            href="https://www.instagram.com/p/CAp_qaQHEuM/"
                                                            title="Instagram"
                                                            target="_blank"
                                                            >
                                                            <img
                                                                src="cid:image4"
                                                                alt="Instagram"
                                                                title="Instagram"
                                                                width="32"
                                                                style="
                                                                outline: none;
                                                                text-decoration: none;
                                                                -ms-interpolation-mode: bicubic;
                                                                clear: both;
                                                                display: block !important;
                                                                border: none;
                                                                height: auto;
                                                                float: none;
                                                                max-width: 32px !important;
                                                                "
                                                            />
                                                            </a>
                                                        </td>
                                                        </tr>
                                                    </tbody>
                                                    </table>
                                                    <!--[if (mso)|(IE)]></td><![endif]-->

                                                    <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 0px;" valign="top"><![endif]-->
                                                    <table
                                                    align="left"
                                                    border="0"
                                                    cellspacing="0"
                                                    cellpadding="0"
                                                    width="32"
                                                    height="32"
                                                    style="
                                                        width: 32px !important;
                                                        height: 32px !important;
                                                        display: inline-block;
                                                        border-collapse: collapse;
                                                        table-layout: fixed;
                                                        border-spacing: 0;
                                                        mso-table-lspace: 0pt;
                                                        mso-table-rspace: 0pt;
                                                        vertical-align: top;
                                                        margin-right: 0px;
                                                    "
                                                    >
                                                    <tbody>
                                                        <tr style="vertical-align: top">
                                                        <td
                                                            align="left"
                                                            valign="middle"
                                                            style="
                                                            word-break: break-word;
                                                            border-collapse: collapse !important;
                                                            vertical-align: top;
                                                            "
                                                        >
                                                            <a
                                                            href="https://discord.gg/QMKHU8y"
                                                            title="Discord"
                                                            target="_blank"
                                                            >
                                                            <img
                                                                src="cid:image6"
                                                                alt="Discord"
                                                                title="Discord"
                                                                width="32"
                                                                style="
                                                                outline: none;
                                                                text-decoration: none;
                                                                -ms-interpolation-mode: bicubic;
                                                                clear: both;
                                                                display: block !important;
                                                                border: none;
                                                                height: auto;
                                                                float: none;
                                                                max-width: 32px !important;
                                                                "
                                                            />
                                                            </a>
                                                        </td>
                                                        </tr>
                                                    </tbody>
                                                    </table>
                                                    <!--[if (mso)|(IE)]></td><![endif]-->

                                                    <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
                                                </div>
                                                </div>
                                            </td>
                                            </tr>
                                        </tbody>
                                        </table>

                                        <table
                                        style="font-family: 'Montserrat', sans-serif"
                                        role="presentation"
                                        cellpadding="0"
                                        cellspacing="0"
                                        width="100%"
                                        border="0"
                                        >
                                        <tbody>
                                            <tr>
                                            <td
                                                style="
                                                overflow-wrap: break-word;
                                                word-break: break-word;
                                                padding: 10px 10px 15px;
                                                font-family: 'Montserrat', sans-serif;
                                                "
                                                align="left"
                                            >
                                                <div
                                                style="
                                                    color: #ffffff;
                                                    line-height: 160%;
                                                    text-align: center;
                                                    word-wrap: break-word;
                                                "
                                                >
                                                <p style="font-size: 14px; line-height: 160%">
                                                    ????? 2022 ??? Todos os direitos reservados<br /><span
                                                    style="
                                                        color: #ffffff;
                                                        font-size: 14px;
                                                        line-height: 22.4px;
                                                    "
                                                    ><a
                                                        rel="noopener"
                                                        href="https://politicas.kiniga.com/termos-de-servico/"
                                                        target="_blank"
                                                        style="color: #ffffff"
                                                        >Termos de Servi??o</a
                                                    ></span
                                                    >
                                                    |
                                                    <span
                                                    style="
                                                        color: #ffffff;
                                                        font-size: 14px;
                                                        line-height: 22.4px;
                                                    "
                                                    ><a
                                                        rel="noopener"
                                                        href="https://politicas.kiniga.com/politicas-de-privacidade/"
                                                        target="_blank"
                                                        style="color: #ffffff"
                                                        >Pol??tica de Privacidade</a
                                                    ></span
                                                    >
                                                </p>
                                                </div>
                                            </td>
                                            </tr>
                                        </tbody>
                                        </table>

                                        <!--[if (!mso)&(!IE)]><!-->
                                    </div>
                                    <!--<![endif]-->
                                    </div>
                                </div>
                                <!--[if (mso)|(IE)]></td><![endif]-->
                                <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
                                </div>
                            </div>
                            </div>

                            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                        </td>
                        </tr>
                    </tbody>
                    </table>
                    <!--[if mso]></div><![endif]-->
                    <!--[if IE]></div><![endif]-->
                </body>
                </html>


            """
            emailtxt = """\
                Esta ?? uma mensagem autom??tica. N??o responda.

                Ol??, como voc?? est???


                Viemos informar que recebemos a sua hist??ria, mas infelizmente n??o poderemos aceit??-la no site, pois nela h?? uma car??ncia dos requisitos m??nimos para que uma hist??ria seja publicada. Mas n??o desanime, voc?? pode nos enviar a hist??ria novamente quando desejar! E n??o se esque??a de revisar bem antes de enviar, beleza?

                Caso tenha d??vidas, temos um FAQ, onde voc?? pode ter um contato com nossa equipe. Mande mensagem para os membros da equipe apenas ap??s ir ao FAQ e jamais entre em contato pelo privado (caso seja preciso, um membro ir?? cham??-lo, nunca o contr??rio).

                (FAQ fixado no chat geral do nosso servidor do discord)

                Link Kiniga: https://discord.gg/dWGvCr3

                Tamb??m temos parceria com o server Novel Brasil, uma comunidade para escritores. L?? voc?? pode encontrar outros autores e pessoas que podem te ajudar a melhorar na escrita, com aulas em calls, conversa com tutores e artigos do blog que eles possuem.

                Link Novel Brasil: https://discord.gg/2yEkSWdM9z

                Em todo caso, espero que tenha um dia muito produtivo escrevendo!
                
                """

        return email, emailtxt
