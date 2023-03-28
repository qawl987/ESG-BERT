def grammer(x, folder_name, file):
    if x == 'test' and folder_name == 'test' and file == 'test':
        print('test')
        return
    assert folder_name == 'american_pdf' or 'taiwan_pdf', 'nation false'
    if folder_name == 'american_pdf':
        if file == '01_dow_1_85':
            return None if x[:15] == 'VISION STRATEGY' or x[:25] == 'ENVIRONMENTAL PERFORMANCE' or x[:17] == 'DOW      2021 ESG' else x
        elif file == '03_amazon_1_79':
            return None if x[:45] == '2021 Sustainability Report       Introduction' else x
        elif file == '04_apple_1_72':
            return None if x[:22] == 'Apples 2022 ESG Report' else x
        elif file == '05_boeing_1_66':
            return None if x[:26] == '2022 Sustainability Report' else x
        elif file == '06_bxp_1_65':
            return None if x[:25] == '2021 ENVIRONMENTAL SOCIAL' else x
        elif file == '07_charles_1_50':
            return None if x[:18] == 'The Charles Schwab' or x[:26] == 'Back to table of contents' else x
        elif file == '08_cisco_1_56':
            return None if x[:25] == '2022 Cisco Purpose Report' else x
        elif file == '09_citigroup_1_137':
            return None if x[:20] == 'CITI 2021 ESG REPORT' else x
        elif file == '10_cme_1_34':
            return None if x[:25] == '2021 CME GROUP ESG REPORT' else x
        elif file == '11_colgate_1_84':
            return None if x[:37] == '2 0 2 1   S U S T A I N A B I L I T Y' or x[:7] == 'P A G E' else x
        elif file == '12_corning_1_71':
            return None if x[:27] == '2021 Corning Sustainability' or x[:18] == 'DRAFT REPORT March' else x
        elif file == '14_eei_1_80':
            return None if x[-23:] == 'EEI Investor ESG Report' else x
        elif file == '15_itt_1_44':
            return None if x[:30] == '2022 ITT Sustainability Report' else x
        elif file == '16_fedex_1_34':
            return None if x[:19] == 'N T R O D U C T O N' or x[:21] == 'O U R P R N C P L E S' or x[:17] == 'O U R P L A N E T' or x[:17] == 'O U R P E O P L E' or x[:21] == 'D A T A A P P E N D X'else x
        elif file == '17_firstscolar_1_57':
            return None if x[:33] == 'First Solar Sustainability Report' else x
        elif file == '20_jpmorgan_1_61':
            return None if x[:16] == 'Message from Our' or x[:23] == 'Feature Our 25 Trillion' else x
        elif file == '25_visa_1_52':
            return None if x[:18] == '2021 Environmental' else x
        else:
            return x
    elif folder_name == 'taiwan_pdf':
        if file == '01_umc_1_154':
            return None if x[:32] == 'Leading the Corporate Governance' or x[:36] == '2020 CORPORATE SOCIAL RESPONSIBILITY' else x
        elif file == '02_tsmc_1_210':
            return None if x[:37] == '2021 Sustainability ReportESG Feature' else x
        elif file == '03_macronix_1_114':
            return None if x[:37] == 'Messages from the Macronix Executives' else x
        elif file == '05_eme_1_46':
            return None if x[:13] == 'About eMemory' else x
        elif file == '06_asus_1_108':
            return None if x[:20] == '00 About This Report' else x
        elif file == '07_acer_1_127':
            return None if x[:33] == 'Message from the Chairman and CEO' or x[:33] == 'A Tolerant Workplace  and Society' else x
        elif file == '08_witron_1_93':
            return None if x[:27] == '2021 Wistron ITS ESG Report' else x
        elif file == '10_compal_1_169':
            return None if x[:33] == 'Climate change and GHG Management' else x
        elif file == '13_csc_1_150':
            return None if x[:23] == '2021 CSC Sustainability' or x[:12] == 'CH 4Industry' else x
        elif file == '16_gigabyte_1_74':
            return None if x[:24] == 'Sustainable  Development' or x[:40] == '2021 GIGABYTE Technology  Sustainability' else x
        elif file == '18_novatek_1_140':
            return None if x[:9] == 'CH1CH2CH4' else x
        elif file == '19_mediatek_1_97':
            return None if x[:26] == '2021 Sustainability Report' else x
        elif file == '21_cathay_1_52':
            return None if x[:25] == 'Cathay Financial Holdings' else x
        elif file == '22_cht_1_79':
            return None if x[:23] == 'Corporate Governance 18' or x[:16] == 'THE CREATION  OF' or x[:25] == 'Emerging Opportunities 48' or x[:32] == 'The Digital Economy Motivator 64' or x[:32] == 'The Happiness Value Protector 74' else x
        elif file == '23_fubon_1_89':
            return None if x[:31] == 'Chairmans MessageSustainability' or x[:35] == 'Fubon Financial 2021 Sustainability' or x[-26:] == '2021 Sustainability Report' else x
        elif file == '24_mega_1_68':
            return None if x[-39:] == '2021 Mega Holding Sustainability Report' or x[:39] == '2021 Mega Holding Sustainability Report' or x[-26:] == '2021 Sustainability Report' else x
        else:
            return x
    