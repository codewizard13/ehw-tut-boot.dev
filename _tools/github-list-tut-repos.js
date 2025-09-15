/**
 * Node.js CommonJS script to fetch all repositories for the authenticated user
 * and filter those containing 'tut' in the repository name.
 *
 * Usage:
 * 1. Install dependencies: npm install @octokit/rest
 * 2. Set environment variable: export GITHUB_TOKEN=your_personal_access_token
 * 3. Run the script: node github-list-tut-repos.js
 */

(async () => {
  // Dynamically import the ES module in CommonJS context
  const { Octokit } = await import("@octokit/rest");

  // Get the token from environment variable
  const token = process.env.GITHUB_TOKEN;
  if (!token) {
    console.error("Please set your GITHUB_TOKEN environment variable.");
    process.exit(1);
  }

  const octokit = new Octokit({ auth: token });

  try {
    // Get the logged-in user's username
    const { data: user } = await octokit.rest.users.getAuthenticated();
    const username = user.login;

    // Paginate through all repos
    let repos = [];
    let page = 1;
    let hasMore = true;

    while (hasMore) {
      const { data } = await octokit.rest.repos.listForUser({
        username,
        per_page: 100,
        page,
      });
      repos = repos.concat(data);
      hasMore = data.length === 100;
      page += 1;
    }

    // Filter repos whose name contains 'tut'
    const filtered = repos.filter(repo => repo.name.includes('tut'));

    // Print the filtered repos
    console.log("Repositories containing 'tut' in their name:");
    filtered.forEach(repo => {
      console.log(`- ${repo.name}: ${repo.html_url}`);
    });
  } catch (error) {
    console.error("Error fetching repositories:", error.message);
    process.exit(1);
  }
})();