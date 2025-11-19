"""
Event loop pokreće funkciju main i u njoj se stvaraju tri taska pomoću asyncio create_task, 
čime se korutine odmah zakazuju i prelaze iz stanja pending u running. Svaki timer odmah ispiše 
koliko je sekundi ostalo i zatim naiđe na await asyncio sleep 1, gdje se korutina pauzira i 
prelazi u stanje čekanja, a event loop prelazi na drugi task. Svake sekunde event loop "budi"
sve timere koji su čekali, oni opet ispišu preostalo vrijeme i ponovno se pauziraju. 
Timer 1 završava nakon 3 sekunde, Timer 2 nakon 5, a Timer 3 nakon 7 sekundi, pri čemu 
svaki nakon isteka vremena ispiše završnu poruku i prelazi u stanje done. Kada su sva tri 
taska dovršena, asyncio gather u main također završava, main se gasi i time se cijeli event loop završava.
"""