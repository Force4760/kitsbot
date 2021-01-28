#html list of kits
def subtt(lists):
    i = 0
    output = ""
    for kit in lists:
        i += 1
        output += f"""
        <li>
        <section class="kit">
            <h3 class="title">{i} {str(kit[0]).replace("<", " ").replace(">", " ")}</h3>
            <div class="info">
                <ul>
                <li><p class="date"> {kit[1]}</p></li>
                <li><p class="author"> By: {str(kit[2]).replace("<", " ").replace(">", " ")}</p></li>
                <li><p class="score"> Score: {str(kit[3]).replace("<", " ").replace(">", " ")}</p></li>
                <li><a href="{kit[4]}" target="_blank" class="l">Download</a></li>
                </ul>
            </div>
        </section>
        </li>
        """
        

    return output