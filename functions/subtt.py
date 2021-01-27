#html list of kits
def subtt(lists):
    output = ""
    for kit in lists:
        output += f"""
        <section class="kit">
            <h3 class="title">{str(kit[0]).replace("<", " ").replace(">", " ")}</h3>
            <div class="info">
                <p class="date">{kit[1]}</p>
                <p class="author">By: {str(kit[2]).replace("<", " ").replace(">", " ")}</p>
                <a href="{kit[3]}" target="_blank" class="l">Download</a>
            </div>
        </section>
        """
    return output