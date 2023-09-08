{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "96849357",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Address already in use\n",
      "Port 5000 is in use by another program. Either identify and stop that program, or start the server with a different port.\n",
      "On macOS, try disabling the 'AirPlay Receiver' service from System Preferences -> Sharing.\n"
     ]
    },
    {
     "ename": "AssertionError",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mOSError\u001b[0m                                   Traceback (most recent call last)",
      "File \u001b[0;32m~/anaconda3/lib/python3.10/site-packages/werkzeug/serving.py:911\u001b[0m, in \u001b[0;36mprepare_socket\u001b[0;34m(hostname, port)\u001b[0m\n\u001b[1;32m    910\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m--> 911\u001b[0m     \u001b[43ms\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mbind\u001b[49m\u001b[43m(\u001b[49m\u001b[43mserver_address\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    912\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mOSError\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m e:\n",
      "\u001b[0;31mOSError\u001b[0m: [Errno 48] Address already in use",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mSystemExit\u001b[0m                                Traceback (most recent call last)",
      "    \u001b[0;31m[... skipping hidden 1 frame]\u001b[0m\n",
      "Cell \u001b[0;32mIn[3], line 70\u001b[0m\n\u001b[1;32m     69\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;18m__name__\u001b[39m \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m__main__\u001b[39m\u001b[38;5;124m'\u001b[39m:\n\u001b[0;32m---> 70\u001b[0m     \u001b[43mapp\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrun\u001b[49m\u001b[43m(\u001b[49m\u001b[43mdebug\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43;01mTrue\u001b[39;49;00m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.10/site-packages/flask/app.py:1188\u001b[0m, in \u001b[0;36mFlask.run\u001b[0;34m(self, host, port, debug, load_dotenv, **options)\u001b[0m\n\u001b[1;32m   1187\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m-> 1188\u001b[0m     \u001b[43mrun_simple\u001b[49m\u001b[43m(\u001b[49m\u001b[43mt\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mcast\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mstr\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mhost\u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mport\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43moptions\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m   1189\u001b[0m \u001b[38;5;28;01mfinally\u001b[39;00m:\n\u001b[1;32m   1190\u001b[0m     \u001b[38;5;66;03m# reset the first request information if the development server\u001b[39;00m\n\u001b[1;32m   1191\u001b[0m     \u001b[38;5;66;03m# reset normally.  This makes it possible to restart the server\u001b[39;00m\n\u001b[1;32m   1192\u001b[0m     \u001b[38;5;66;03m# without reloader and that stuff from an interactive shell.\u001b[39;00m\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.10/site-packages/werkzeug/serving.py:1062\u001b[0m, in \u001b[0;36mrun_simple\u001b[0;34m(hostname, port, application, use_reloader, use_debugger, use_evalex, extra_files, exclude_patterns, reloader_interval, reloader_type, threaded, processes, request_handler, static_files, passthrough_errors, ssl_context)\u001b[0m\n\u001b[1;32m   1061\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m is_running_from_reloader():\n\u001b[0;32m-> 1062\u001b[0m     s \u001b[38;5;241m=\u001b[39m \u001b[43mprepare_socket\u001b[49m\u001b[43m(\u001b[49m\u001b[43mhostname\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mport\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m   1063\u001b[0m     fd \u001b[38;5;241m=\u001b[39m s\u001b[38;5;241m.\u001b[39mfileno()\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.10/site-packages/werkzeug/serving.py:930\u001b[0m, in \u001b[0;36mprepare_socket\u001b[0;34m(hostname, port)\u001b[0m\n\u001b[1;32m    924\u001b[0m             \u001b[38;5;28mprint\u001b[39m(\n\u001b[1;32m    925\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mOn macOS, try disabling the \u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mAirPlay Receiver\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m    926\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m service from System Preferences -> Sharing.\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m    927\u001b[0m                 file\u001b[38;5;241m=\u001b[39msys\u001b[38;5;241m.\u001b[39mstderr,\n\u001b[1;32m    928\u001b[0m             )\n\u001b[0;32m--> 930\u001b[0m     \u001b[43msys\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mexit\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m1\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[1;32m    932\u001b[0m s\u001b[38;5;241m.\u001b[39mlisten(LISTEN_QUEUE)\n",
      "\u001b[0;31mSystemExit\u001b[0m: 1",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mAssertionError\u001b[0m                            Traceback (most recent call last)",
      "    \u001b[0;31m[... skipping hidden 1 frame]\u001b[0m\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.10/site-packages/IPython/core/interactiveshell.py:2047\u001b[0m, in \u001b[0;36mInteractiveShell.showtraceback\u001b[0;34m(self, exc_tuple, filename, tb_offset, exception_only, running_compiled_code)\u001b[0m\n\u001b[1;32m   2044\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m exception_only:\n\u001b[1;32m   2045\u001b[0m     stb \u001b[38;5;241m=\u001b[39m [\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mAn exception has occurred, use \u001b[39m\u001b[38;5;124m%\u001b[39m\u001b[38;5;124mtb to see \u001b[39m\u001b[38;5;124m'\u001b[39m\n\u001b[1;32m   2046\u001b[0m            \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mthe full traceback.\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m'\u001b[39m]\n\u001b[0;32m-> 2047\u001b[0m     stb\u001b[38;5;241m.\u001b[39mextend(\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mInteractiveTB\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget_exception_only\u001b[49m\u001b[43m(\u001b[49m\u001b[43metype\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m   2048\u001b[0m \u001b[43m                                                     \u001b[49m\u001b[43mvalue\u001b[49m\u001b[43m)\u001b[49m)\n\u001b[1;32m   2049\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[1;32m   2050\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m   2051\u001b[0m         \u001b[38;5;66;03m# Exception classes can customise their traceback - we\u001b[39;00m\n\u001b[1;32m   2052\u001b[0m         \u001b[38;5;66;03m# use this in IPython.parallel for exceptions occurring\u001b[39;00m\n\u001b[1;32m   2053\u001b[0m         \u001b[38;5;66;03m# in the engines. This should return a list of strings.\u001b[39;00m\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.10/site-packages/IPython/core/ultratb.py:585\u001b[0m, in \u001b[0;36mListTB.get_exception_only\u001b[0;34m(self, etype, value)\u001b[0m\n\u001b[1;32m    577\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mget_exception_only\u001b[39m(\u001b[38;5;28mself\u001b[39m, etype, value):\n\u001b[1;32m    578\u001b[0m     \u001b[38;5;124;03m\"\"\"Only print the exception type and message, without a traceback.\u001b[39;00m\n\u001b[1;32m    579\u001b[0m \n\u001b[1;32m    580\u001b[0m \u001b[38;5;124;03m    Parameters\u001b[39;00m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    583\u001b[0m \u001b[38;5;124;03m    value : exception value\u001b[39;00m\n\u001b[1;32m    584\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[0;32m--> 585\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mListTB\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mstructured_traceback\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43metype\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mvalue\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.10/site-packages/IPython/core/ultratb.py:452\u001b[0m, in \u001b[0;36mListTB.structured_traceback\u001b[0;34m(self, etype, evalue, etb, tb_offset, context)\u001b[0m\n\u001b[1;32m    449\u001b[0m     chained_exc_ids\u001b[38;5;241m.\u001b[39madd(\u001b[38;5;28mid\u001b[39m(exception[\u001b[38;5;241m1\u001b[39m]))\n\u001b[1;32m    450\u001b[0m     chained_exceptions_tb_offset \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m0\u001b[39m\n\u001b[1;32m    451\u001b[0m     out_list \u001b[38;5;241m=\u001b[39m (\n\u001b[0;32m--> 452\u001b[0m         \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mstructured_traceback\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m    453\u001b[0m \u001b[43m            \u001b[49m\u001b[43metype\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mevalue\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m(\u001b[49m\u001b[43metb\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mchained_exc_ids\u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    454\u001b[0m \u001b[43m            \u001b[49m\u001b[43mchained_exceptions_tb_offset\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mcontext\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    455\u001b[0m         \u001b[38;5;241m+\u001b[39m chained_exception_message\n\u001b[1;32m    456\u001b[0m         \u001b[38;5;241m+\u001b[39m out_list)\n\u001b[1;32m    458\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m out_list\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.10/site-packages/IPython/core/ultratb.py:1118\u001b[0m, in \u001b[0;36mAutoFormattedTB.structured_traceback\u001b[0;34m(self, etype, value, tb, tb_offset, number_of_lines_of_context)\u001b[0m\n\u001b[1;32m   1116\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[1;32m   1117\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mtb \u001b[38;5;241m=\u001b[39m tb\n\u001b[0;32m-> 1118\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mFormattedTB\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mstructured_traceback\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m   1119\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43metype\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mvalue\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mtb\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mtb_offset\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mnumber_of_lines_of_context\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.10/site-packages/IPython/core/ultratb.py:1012\u001b[0m, in \u001b[0;36mFormattedTB.structured_traceback\u001b[0;34m(self, etype, value, tb, tb_offset, number_of_lines_of_context)\u001b[0m\n\u001b[1;32m   1009\u001b[0m mode \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mmode\n\u001b[1;32m   1010\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m mode \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mverbose_modes:\n\u001b[1;32m   1011\u001b[0m     \u001b[38;5;66;03m# Verbose modes need a full traceback\u001b[39;00m\n\u001b[0;32m-> 1012\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mVerboseTB\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mstructured_traceback\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m   1013\u001b[0m \u001b[43m        \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43metype\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mvalue\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mtb\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mtb_offset\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mnumber_of_lines_of_context\u001b[49m\n\u001b[1;32m   1014\u001b[0m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m   1015\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m mode \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mMinimal\u001b[39m\u001b[38;5;124m'\u001b[39m:\n\u001b[1;32m   1016\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m ListTB\u001b[38;5;241m.\u001b[39mget_exception_only(\u001b[38;5;28mself\u001b[39m, etype, value)\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.10/site-packages/IPython/core/ultratb.py:865\u001b[0m, in \u001b[0;36mVerboseTB.structured_traceback\u001b[0;34m(self, etype, evalue, etb, tb_offset, number_of_lines_of_context)\u001b[0m\n\u001b[1;32m    856\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mstructured_traceback\u001b[39m(\n\u001b[1;32m    857\u001b[0m     \u001b[38;5;28mself\u001b[39m,\n\u001b[1;32m    858\u001b[0m     etype: \u001b[38;5;28mtype\u001b[39m,\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    862\u001b[0m     number_of_lines_of_context: \u001b[38;5;28mint\u001b[39m \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m5\u001b[39m,\n\u001b[1;32m    863\u001b[0m ):\n\u001b[1;32m    864\u001b[0m     \u001b[38;5;124;03m\"\"\"Return a nice text document describing the traceback.\"\"\"\u001b[39;00m\n\u001b[0;32m--> 865\u001b[0m     formatted_exception \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mformat_exception_as_a_whole\u001b[49m\u001b[43m(\u001b[49m\u001b[43metype\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mevalue\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43metb\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mnumber_of_lines_of_context\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    866\u001b[0m \u001b[43m                                                           \u001b[49m\u001b[43mtb_offset\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    868\u001b[0m     colors \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mColors  \u001b[38;5;66;03m# just a shorthand + quicker name lookup\u001b[39;00m\n\u001b[1;32m    869\u001b[0m     colorsnormal \u001b[38;5;241m=\u001b[39m colors\u001b[38;5;241m.\u001b[39mNormal  \u001b[38;5;66;03m# used a lot\u001b[39;00m\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.10/site-packages/IPython/core/ultratb.py:799\u001b[0m, in \u001b[0;36mVerboseTB.format_exception_as_a_whole\u001b[0;34m(self, etype, evalue, etb, number_of_lines_of_context, tb_offset)\u001b[0m\n\u001b[1;32m    796\u001b[0m \u001b[38;5;28;01massert\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(tb_offset, \u001b[38;5;28mint\u001b[39m)\n\u001b[1;32m    797\u001b[0m head \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mprepare_header(etype, \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mlong_header)\n\u001b[1;32m    798\u001b[0m records \u001b[38;5;241m=\u001b[39m (\n\u001b[0;32m--> 799\u001b[0m     \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget_records\u001b[49m\u001b[43m(\u001b[49m\u001b[43metb\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mnumber_of_lines_of_context\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mtb_offset\u001b[49m\u001b[43m)\u001b[49m \u001b[38;5;28;01mif\u001b[39;00m etb \u001b[38;5;28;01melse\u001b[39;00m []\n\u001b[1;32m    800\u001b[0m )\n\u001b[1;32m    802\u001b[0m frames \u001b[38;5;241m=\u001b[39m []\n\u001b[1;32m    803\u001b[0m skipped \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m0\u001b[39m\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.10/site-packages/IPython/core/ultratb.py:854\u001b[0m, in \u001b[0;36mVerboseTB.get_records\u001b[0;34m(self, etb, number_of_lines_of_context, tb_offset)\u001b[0m\n\u001b[1;32m    848\u001b[0m     formatter \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[1;32m    849\u001b[0m options \u001b[38;5;241m=\u001b[39m stack_data\u001b[38;5;241m.\u001b[39mOptions(\n\u001b[1;32m    850\u001b[0m     before\u001b[38;5;241m=\u001b[39mbefore,\n\u001b[1;32m    851\u001b[0m     after\u001b[38;5;241m=\u001b[39mafter,\n\u001b[1;32m    852\u001b[0m     pygments_formatter\u001b[38;5;241m=\u001b[39mformatter,\n\u001b[1;32m    853\u001b[0m )\n\u001b[0;32m--> 854\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mlist\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43mstack_data\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mFrameInfo\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mstack_data\u001b[49m\u001b[43m(\u001b[49m\u001b[43metb\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43moptions\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43moptions\u001b[49m\u001b[43m)\u001b[49m\u001b[43m)\u001b[49m[tb_offset:]\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.10/site-packages/stack_data/core.py:546\u001b[0m, in \u001b[0;36mFrameInfo.stack_data\u001b[0;34m(cls, frame_or_tb, options, collapse_repeated_frames)\u001b[0m\n\u001b[1;32m    530\u001b[0m \u001b[38;5;129m@classmethod\u001b[39m\n\u001b[1;32m    531\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mstack_data\u001b[39m(\n\u001b[1;32m    532\u001b[0m         \u001b[38;5;28mcls\u001b[39m,\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    536\u001b[0m         collapse_repeated_frames: \u001b[38;5;28mbool\u001b[39m \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mTrue\u001b[39;00m\n\u001b[1;32m    537\u001b[0m ) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m Iterator[Union[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mFrameInfo\u001b[39m\u001b[38;5;124m'\u001b[39m, RepeatedFrames]]:\n\u001b[1;32m    538\u001b[0m     \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m    539\u001b[0m \u001b[38;5;124;03m    An iterator of FrameInfo and RepeatedFrames objects representing\u001b[39;00m\n\u001b[1;32m    540\u001b[0m \u001b[38;5;124;03m    a full traceback or stack. Similar consecutive frames are collapsed into RepeatedFrames\u001b[39;00m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    544\u001b[0m \u001b[38;5;124;03m    and optionally an Options object to configure.\u001b[39;00m\n\u001b[1;32m    545\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[0;32m--> 546\u001b[0m     stack \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mlist\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43miter_stack\u001b[49m\u001b[43m(\u001b[49m\u001b[43mframe_or_tb\u001b[49m\u001b[43m)\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    548\u001b[0m     \u001b[38;5;66;03m# Reverse the stack from a frame so that it's in the same order\u001b[39;00m\n\u001b[1;32m    549\u001b[0m     \u001b[38;5;66;03m# as the order from a traceback, which is the order of a printed\u001b[39;00m\n\u001b[1;32m    550\u001b[0m     \u001b[38;5;66;03m# traceback when read top to bottom (most recent call last)\u001b[39;00m\n\u001b[1;32m    551\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m is_frame(frame_or_tb):\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.10/site-packages/stack_data/utils.py:98\u001b[0m, in \u001b[0;36miter_stack\u001b[0;34m(frame_or_tb)\u001b[0m\n\u001b[1;32m     96\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m frame_or_tb:\n\u001b[1;32m     97\u001b[0m     \u001b[38;5;28;01myield\u001b[39;00m frame_or_tb\n\u001b[0;32m---> 98\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[43mis_frame\u001b[49m\u001b[43m(\u001b[49m\u001b[43mframe_or_tb\u001b[49m\u001b[43m)\u001b[49m:\n\u001b[1;32m     99\u001b[0m         frame_or_tb \u001b[38;5;241m=\u001b[39m frame_or_tb\u001b[38;5;241m.\u001b[39mf_back\n\u001b[1;32m    100\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.10/site-packages/stack_data/utils.py:91\u001b[0m, in \u001b[0;36mis_frame\u001b[0;34m(frame_or_tb)\u001b[0m\n\u001b[1;32m     90\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mis_frame\u001b[39m(frame_or_tb: Union[FrameType, TracebackType]) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m \u001b[38;5;28mbool\u001b[39m:\n\u001b[0;32m---> 91\u001b[0m     \u001b[43massert_\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43misinstance\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43mframe_or_tb\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m(\u001b[49m\u001b[43mtypes\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mFrameType\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mtypes\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mTracebackType\u001b[49m\u001b[43m)\u001b[49m\u001b[43m)\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m     92\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(frame_or_tb, (types\u001b[38;5;241m.\u001b[39mFrameType,))\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.10/site-packages/stack_data/utils.py:172\u001b[0m, in \u001b[0;36massert_\u001b[0;34m(condition, error)\u001b[0m\n\u001b[1;32m    170\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(error, \u001b[38;5;28mstr\u001b[39m):\n\u001b[1;32m    171\u001b[0m     error \u001b[38;5;241m=\u001b[39m \u001b[38;5;167;01mAssertionError\u001b[39;00m(error)\n\u001b[0;32m--> 172\u001b[0m \u001b[38;5;28;01mraise\u001b[39;00m error\n",
      "\u001b[0;31mAssertionError\u001b[0m: "
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, render_template\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/', methods=['GET', 'POST'])\n",
    "def index():\n",
    "    if request.method == 'POST':\n",
    "        user_input = request.form['user_input']\n",
    "        # Process user_input using your Python function\n",
    "        processed_result = process_input(user_input)\n",
    "        return render_template('index.html', result=processed_result)\n",
    "    return render_template('index.html', result=None)\n",
    "\n",
    "def song_recommender(df1, df2):\n",
    "    song = input(\"Please enter the name of a song: \")\n",
    "    # Check if the input contains at least one alphabetical character and/or alphanumeric character\n",
    "    if not (any(c.isalpha() for c in song) and any(c.isalnum() for c in song)):\n",
    "        print(\"Invalid input. Please enter a song name containing letters and/or numbers.\")\n",
    "        return\n",
    "    print(f\"You entered a valid song name: {song}\")\n",
    "    # Load Spotify secrets\n",
    "    secrets_file = open(\"secrets.txt\", \"r\")\n",
    "    string = secrets_file.read()\n",
    "    secrets_dict = {}\n",
    "    for line in string.split('\\n'):\n",
    "        if len(line) > 0:\n",
    "            secrets_dict[line.split(':')[0]] = line.split(':')[1].strip()\n",
    "    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=secrets_dict['clientid'],\n",
    "                                                               client_secret=secrets_dict['clientsecret']))\n",
    "    results = sp.search(q='track:' + song, type='track')\n",
    "    track = pd.json_normalize(results[\"tracks\"][\"items\"])\n",
    "    if not track.empty:\n",
    "        song_id = track.iloc[0]['id']\n",
    "        song_url = track.iloc[0]['external_urls.spotify']\n",
    "    else:\n",
    "        print(\"Song not found in Spotify.\")\n",
    "        return\n",
    "    audio_features_list = sp.audio_features(song_id)\n",
    "    audio_features_df = pd.json_normalize(audio_features_list)\n",
    "    audio_features_df = audio_features_df[['duration_ms', 'danceability',\n",
    "                                           'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',\n",
    "                                           'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature']]\n",
    "    # Load scaler and transform data\n",
    "    with open('scaler.pkl', 'rb') as f:\n",
    "        loaded_scaler = pickle.load(f)\n",
    "        X = loaded_scaler.transform(audio_features_df)\n",
    "    # Load KMeans model and predict cluster\n",
    "    with open('kmeans.pkl', 'rb') as f:\n",
    "        loaded_kmeans = pickle.load(f)\n",
    "        clusters = loaded_kmeans.predict(X)\n",
    "    matching_song = df1[(df1['title'].str.lower() == song.lower())]\n",
    "    if not matching_song.empty:\n",
    "        print(f\"The song '{matching_song['title'].values[0]}' by {matching_song['artist'].values[0]} matches your input.\")\n",
    "        recommended_song = df1[df1['title'].str.lower() != song].sample(1)\n",
    "        print(f\"Here's a recommended song: '{recommended_song['title'].values[0]}' by {recommended_song['artist'].values[0]}\")\n",
    "        results2 = sp.search(q='track:' + recommended_song['Title'].values[0], type='track')\n",
    "        track2 = pd.json_normalize(results2[\"tracks\"][\"items\"])\n",
    "        song_url = track2.iloc[0]['external_urls.spotify']\n",
    "        print(f\"Here's a url of the song: {song_url}\")\n",
    "    else:\n",
    "        cluster_df = df2[df2['clusters'] == clusters[0]]\n",
    "        recommended_song2 = cluster_df[cluster_df['track_name'].str.lower() != song].sample(1)\n",
    "        print(f\"Here's a recommended song: '{recommended_song2['track_name'].values[0]}' by {recommended_song2['artists'].values[0]}\")\n",
    "        results3 = sp.search(q='track:' + recommended_song2['track_name'].values[0], type='track')\n",
    "        track3 = pd.json_normalize(results3[\"tracks\"][\"items\"])\n",
    "        song_url = track3.iloc[0]['external_urls.spotify']\n",
    "        print(f\"Here's a url of the song: {song_url}\")\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4f70c6c5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4cb21d93",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e3ca5de8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3363bac0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "390b348a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "01f1c8de",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b06a702a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a44d02d4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "007d1227",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3de6a89e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
