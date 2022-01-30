def link_pse_command(update: Update, _: CallbackContext):
    update.message.reply_text("""\n\n
    🏦 Para pagar por internet puede usar este : \n
    [link de pago por PSE](https://www.mipagoamigo.com/MPA_WebSite/ServicePayments/StartPayment?id=4510&searchedCategoryId=&searchedAgreementName=ACADEMIA%20DE%20LAS%20AMERICAS)"""
        , parse_mode="markdown")
